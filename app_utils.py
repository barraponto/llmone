import os
import streamlit as st

from inference import Inference
from models.config import Config, LLModel


@st.cache_resource
def get_inference(api_key: str, model: LLModel) -> str:
    return Inference(api_key=api_key, model=model)


def init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


def init_chat_ui() -> None:
    st.set_page_config(page_title="LLMOne", page_icon="./favicon.png")


def load_config() -> Config:
    return Config(
        groq_api_key=st.session_state.groq_api_key or os.getenv("GROQ_API_KEY"),
        model=st.session_state.model or LLModel.GROQ_LLAMA_3_1_8B_INSTANT,
    )
