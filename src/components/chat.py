# src/components/chat_component.py

import streamlit as st
from src.models.llm import get_llm

def show_chat_interface() -> None:
    """Renders a chat UI for interacting with the selected LLM."""

    st.header("LLM Chat Playground")

    # If the user hasn't chosen a model yet, show a warning and stop.
    if "selected_model" not in st.session_state:
        st.warning("No model selected yet. Please select a model in the sidebar.")
        return

    # Grab the chosen LLM instance.
    llm = get_llm(st.session_state["selected_model"])

    # Initialize chat history in session state, if not present.
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Display existing chat history.
    for message in st.session_state["chat_history"]:
        role = message["role"]  # "user" or "assistant"
        content = message["content"]

        # The new Chat UI in Streamlit:
        st.chat_message(role).write(content)

    # Provide a chat input box at the bottom. 
    user_input = st.chat_input("Type your message and press Enter...")

    if user_input:
        # 1. Add user's message to chat history
        st.session_state["chat_history"].append(
            {"role": "user", "content": user_input}
        )

        # 2. Get the LLM's response
        response = llm.invoke(user_input)

        # 3. Add the AI's response to the chat history
        st.session_state["chat_history"].append(
            {"role": "assistant", "content": response.content}
        )

        # 4. Trigger a rerun to update the UI
        st.rerun()
