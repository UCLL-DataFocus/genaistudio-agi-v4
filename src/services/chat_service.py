import uuid
import streamlit as st
import importlib
from datetime import datetime
from typing import List, cast

from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import BaseMessage
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from pydantic import BaseModel, Field

from src.models.llm import get_llm

#############################
# In-Memory History Storage #
#############################

class InMemoryHistory(BaseModel):
    messages: List[BaseMessage] = Field(default_factory=list)

    def add_messages(self, messages: List[BaseMessage]) -> None:
        self.messages.extend(messages)

    def clear(self) -> None:
        self.messages = []

# Global store for histories, keyed by session_id
_history_store = {}

def get_session_history(session_id: str) -> InMemoryHistory:
    if session_id not in _history_store:
        _history_store[session_id] = InMemoryHistory()
    return _history_store[session_id]

###############################
# Chat Session Initialization #
###############################

def init_chat_session() -> None:
    """Initializes the chat session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "show_suggestions" not in st.session_state:
        st.session_state.show_suggestions = True
    if "awaiting_response" not in st.session_state:
        st.session_state.awaiting_response = None
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

def handle_new_chat() -> None:
    """Resets chat and suggestions and clears the in-memory history."""
    st.session_state["messages"] = []
    st.session_state["show_suggestions"] = True
    st.session_state["awaiting_response"] = None
    session_id = st.session_state["session_id"]
    if session_id:
        get_session_history(session_id).clear()
    st.rerun()

def get_suggested_questions() -> list[str]:
    """Returns suggested questions."""
    return ["Test", "Test 2"]

def handle_chat_interaction(user_input: str) -> None:
    """Handles both user-typed messages and suggested questions."""
    if not user_input:
        return

    st.session_state["show_suggestions"] = False

    if st.session_state["awaiting_response"]:
        response = chat_with_gpt(st.session_state["awaiting_response"])
        st.session_state["messages"].append({"role": "assistant", "content": response})
        st.session_state["awaiting_response"] = None
        st.rerun()

    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.session_state["awaiting_response"] = user_input
    st.rerun()

#######################################
# Chat with LLM Using Memory-Enabled  #
#######################################

def chat_with_gpt(user_input: str) -> str:
    """Processes user input with chat history and returns the LLM's response."""
    session_id = st.session_state.get("session_id")

    # Load the system message template from the language-specific module
    prompt_module = importlib.import_module(f"src.prompts.prompt")
    system_message_template = prompt_module.TEMPLATE

    # Create a prompt with system message, chat history, and user input
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message_template),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{user_input}"),
    ])

    # Retrieve the selected LLM
    llm = get_llm(st.session_state["selected_model"])

    # Build the chain: prompt template piped into the LLM
    chain = prompt | llm

    # Wrap the chain with RunnableWithMessageHistory for history management
    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="user_input",
        history_messages_key="chat_history",
    )

    # Prepare input data with the current date
    today_str = datetime.now().strftime("%Y-%m-%d")
    input_data = {"user_input": user_input, "today": today_str}

    # Configuration for session-specific history
    config = {"configurable": {"session_id": session_id}}

    try:
        response = chain_with_history.invoke(input_data, config=config)
        response_str = cast(str, response.content)
    except Exception as e:
        response_str = f"Error: {e}"

    return response_str