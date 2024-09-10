from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st


# 환경 변수에서 API 키 로드
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
model = 'gpt-4o-mini' # gpt-3.5-turbo

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

    client = OpenAI(api_key=api_key)

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=model, messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)