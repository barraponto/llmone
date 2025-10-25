import os
import streamlit as st

from app_utils import get_inference, init_session_state
from messages import Message


init_session_state()
inference = get_inference(os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="LLMOne",
    page_icon="./favicon.png",
)

user = st.chat_message("user")
llmone = st.chat_message("llmone", avatar="./favicon.png")

prompt = st.chat_input("Enter your message here")

if prompt:
    st.session_state.messages.append(Message(role="user", content=prompt))
    response = inference.chat(prompt)
    st.session_state.messages.append(Message(role="llmone", content=response))

for message in st.session_state.messages:
    match message.role:
        case "user":
            user.write(message.content)
        case "llmone":
            llmone.write(message.content)
