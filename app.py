import os
import streamlit as st

from app_utils import get_inference, init_chat_ui, init_session_state
from models.config import LLModel
from models.messages import Message


init_session_state()
init_chat_ui()

with st.sidebar:
    """# Settings"""
    groq_api_key = st.text_input("Groq API Key", type="password")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    model = st.selectbox("Model", LLModel)

inference = get_inference(os.getenv("GROQ_API_KEY"), model=model)
prompt = st.chat_input("Enter your message here")


if prompt:
    st.session_state.messages.append(Message(role="user", content=prompt))
    response = inference.chat(prompt)
    st.session_state.messages.append(Message(role="llmone", content=response))

for message in st.session_state.messages:
    match message.role:
        case "user":
            st.chat_message("user").write(message.content)
        case "llmone":
            st.chat_message("llmone", avatar="./favicon.png").write(message.content)
