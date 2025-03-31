# src/components/llm_component.py
import streamlit as st
from src.models.llm import list_supported_models

def show_llm_ui() -> None:
    """
    Displays UI elements for selecting and using LLMs.
    """
    st.sidebar.title("Model Selectie")
    model_options = list_supported_models()
    
    # Check if any models are available
    if not model_options:
        st.sidebar.warning("No LLMs are currently supported. Please check your .env.secret file.")
        return

    # Let user select a model
    st.sidebar.selectbox(
        "Kies een model:",
        options=model_options,
        index=1,
        key="selected_model",
    )