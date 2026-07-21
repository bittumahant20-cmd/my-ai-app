import streamlit as st
import google.generativeai as genai

st.title("🤖 Mera Personal AI Assistant")

api_key = st.text_input("Apni Gemini API Key yahan dalein:", type="password")
user_question = st.text_input("Apna sawal likhein:")

if st.button("AI se Poochein"):
    if not api_key:
        st.error("Pehle API key dalein!")
    elif not user_question:
        st.warning("Kuch sawal toh likhein!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_question)

            st.success("Jawab:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
