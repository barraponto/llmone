import streamlit as st

from inference import Inference


@st.cache_resource
def get_inference(api_key: str) -> str:
    return Inference(api_key=api_key, model="llama-3.1-8b-instant")


def init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []
