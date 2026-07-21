import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mera Personal AI Assistant", page_icon="🤖")

st.title("🤖 Mera Personal AI Assistant")

# API Key input
api_key = st.text_input("Apni Gemini API Key yahan dalein:", type="password")

user_question = st.text_area("Apna sawal likhein:")

if st.button("AI se Poochein"):
    if not api_key:
        st.error("Pehle apni Gemini API Key dalein!")
    elif not user_question:
        st.error("Pehle apna sawal toh likhein!")
    else:
        try:
            # Purana aur sabse safe tarika configuration ka
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            with st.spinner("Jawab ban raha hai..."):
                response = model.generate_content(user_question)
                
            st.success("Jawab:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Error aa gaya: {e}")
