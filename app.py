import streamlit as st
from src.components.model_selection import show_llm_ui
from src.components.chat import show_chat_interface





def app():
    sidebar_logo = "Images/genai-studio-logo.png"

    st.logo(sidebar_logo, icon_image=sidebar_logo, size="large")
    st.set_page_config(
        page_title="Tabblad titel",
        page_icon="Images/genai-studio-favicon.ico",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={"About": "Deze app werd gemaakt door GenAI Studio."},
    )

    st.title("AGI-v4")
    st.write("""A Python app that reticulates splines.""")

    st.sidebar.markdown(
        """
    ### Hoe het werkt
    
    Extra info in markdown.
    """
    )
    # Show LLM selection UI
    show_llm_ui()
    show_chat_interface()
  
if __name__ == "__main__":
    app()

