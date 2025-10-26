import os
import streamlit as st

from inference import Inference
from models.config import Config, GroqModel


@st.cache_resource
def get_inference(config: Config) -> Inference:
    return Inference(config=config)


def init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


def init_chat_ui() -> None:
    st.set_page_config(page_title="LLMOne", page_icon="./favicon.png")


def load_config() -> Config:
    return Config(
        groq_api_key=st.session_state.groq_api_key or os.getenv("GROQ_API_KEY"),
        openai_api_key=st.session_state.openai_api_key or os.getenv("OPENAI_API_KEY"),
        model=st.session_state.model or GroqModel.GROQ_LLAMA_3_1_8B_INSTANT,
    )
