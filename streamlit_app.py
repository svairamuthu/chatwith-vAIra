import streamlit as st
from langchain.llms import OpenAI

st.title("🦜🔗 Ask vAIra")

openai_api_key = st.sidebar.text_input('OpenAI API Key')


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What is Gen AI?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)
