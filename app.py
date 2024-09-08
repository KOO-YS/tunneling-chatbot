import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st


# 환경 변수에서 API 키 로드
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

with st.sidebar:
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Gemini")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not api_key:
        st.info("Please add your GPT API key to continue.")
        st.stop()

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = model.generate_content(prompt)
    msg = response.text
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)