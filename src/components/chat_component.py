import time
from src.components.model_selection import show_llm_ui
import streamlit as st

from src.services.chat_service import chat_with_gpt, get_suggested_questions, handle_chat_interaction, handle_new_chat, init_chat_session

def show_chat_interface() -> None:
    """Renders a chat UI for interacting with the selected LLM."""

    col_title, col_reset = st.columns([0.85, 0.15])
    with col_title:
        st.header("AGI Chatbot")
    with col_reset:
        st.write("")
        if st.button("🔄 Reset"):
            handle_new_chat()
            
    init_chat_session()
    show_llm_ui()


    # If the user hasn't chosen a model yet, show a warning and stop.
    if "selected_model" not in st.session_state:
        st.warning("No model selected yet. Please select a model in the sidebar.")
        return

    suggestions_container = st.empty()
    if st.session_state["show_suggestions"] and not st.session_state["messages"]:
        with suggestions_container:
            questions = get_suggested_questions()
            if questions:
                cols = st.columns(min(len(questions), 4))
                for i, question in enumerate(questions):
                    if cols[i % len(cols)].button(question, key=f"question_{i}"):
                        suggestions_container.empty()
                        handle_chat_interaction(question)
    else:
        suggestions_container.empty()

    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    if st.session_state["awaiting_response"]:
        suggestions_container.empty()
        handle_chat_interaction(st.session_state["awaiting_response"])

    user_input = st.chat_input("Ask a question")
    if user_input:
        suggestions_container.empty()
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        response = "Bedankt voor je slimme vraag of instructie, ik start mijn onderzoek en kom zodadelijk bij je terug!"
        st.session_state["messages"].append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

        st.session_state['start_time'] = time.time()
            
        st.session_state["Disable_abort_button"] = True
        if st.button("Abort", disabled = st.session_state["Disable_abort_button"], key="abort button"):
            st.write("Aborting...")
        with st.status("Verwerken...", expanded=True):
            st.write("boodschap...")
            time.sleep(10)
            st.session_state["Disable_abort_button"] = False
            st.write("boodschap...")
            time.sleep(10)
            st.write("boodschap...")
