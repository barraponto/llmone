import streamlit as st

from app_utils import get_inference, init_chat_ui, init_session_state, load_config
from models.config import model_choices
from models.messages import Message


init_session_state()
init_chat_ui()

with st.sidebar:
    """# Settings"""
    groq_api_key = st.text_input("Groq API Key", type="password", key="groq_api_key")
    openai_api_key = st.text_input(
        "OpenAI API Key", type="password", key="openai_api_key"
    )
    model = st.selectbox("Model", model_choices, key="model")

inference = get_inference(load_config())
prompt = st.chat_input("Enter your message here")


if prompt:
    st.session_state.messages.append(Message(role="user", content=prompt))
    with st.spinner("Thinking..."):
        try:
            response = inference.chat(prompt)
            st.session_state.messages.append(Message(role="llmone", content=response))
        except Exception as e:
            st.error(f"Error: {e}")

for message in st.session_state.messages:
    match message.role:
        case "user":
            st.chat_message("user").write(message.content)
        case "llmone":
            st.chat_message("llmone", avatar="./favicon.png").write(message.content)
