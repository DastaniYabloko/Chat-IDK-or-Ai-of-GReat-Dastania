import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

load_dotenv()
API_KEY = st.secrets.get("GROQ_API_KEY")
MODEL = "openai/gpt-oss-120b"

client = Groq(api_key=API_KEY)

st.set_page_config(
    page_title="Chat IDK",
    page_icon="A"
)

st.title("Тестовый чат") 

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Здравствуй пользователь Я ИИ Великой Дастании! Чем могу помочь?"
        }
        ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Напиши что то . . . ")

if user_input:
    st.session_state.messages.append(
      {
        "role": "user",
        "content": user_input
      }
    )
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        request = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages,
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=1,
            reasoning_effort="medium",
            stream=False,
            stop=None,
            tools=[{"type":"browser_search"}]
        )
        
        assistant_ans = request.choices[0].message.content
        
        st.markdown(assistant_ans)
        
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_ans
        }
    )
        
    
