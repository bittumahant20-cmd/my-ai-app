import streamlit as st
from google import genai

st.set_page_config(page_title="Mera Personal AI Assistant", page_icon="🤖")

st.title("🤖 Mera Personal AI Assistant")

# Sidebar me API Key aur Clear button
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Apni Gemini API Key dalein:", type="password")
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Chat history state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani messages screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Niche chat input box (jaise ChatGPT me hota hai)
if user_question := st.chat_input("Yahan apna sawal likhein..."):
    if not api_key:
        st.sidebar.error("Pehle sidebar me API Key dalein!")
    else:
        st.session_state.messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)

        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model='gemini-3.5-flash',
                contents=user_question,
            )
            
            ai_response = response.text
            
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            with st.chat_message("assistant"):
                st.markdown(ai_response)
                
        except Exception as e:
            st.error(f"Error: {e}")
