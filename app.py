# app.py (Streamlit Urdu Gemini Chatbot - Text Only)

import os
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
from pydub import AudioSegment
import tempfile
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat(history=[])

# UI Config
st.set_page_config(page_title="🤖 Urdu Gemini Chatbot")
st.title("🤖 Urdu Gemini Chatbot")
st.markdown("Type to chat in **Urdu** 🕌")

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input only
user_input = st.chat_input("Type something in Urdu...")

# Send to Gemini and get reply
if user_input:
    with st.spinner("🤖 Soch raha hoon..."):
        prompt = f"Urdu mein chatbot ban kar jawab dein: {user_input}"
        try:
            response = chat.send_message(prompt)
            reply = response.text.strip()
            st.session_state.chat_history.append(("🧕🏻 Tum", user_input))
            st.session_state.chat_history.append(("🤖 GPT", reply))
        except Exception as e:
            reply = f"❌ Error: {e}"
            st.session_state.chat_history.append(("🤖 GPT", reply))

# Display chat history
for role, msg in st.session_state.chat_history:
    with st.chat_message("user" if "Tum" in role else "assistant"):
        st.markdown(msg)

# Speak the latest GPT response
if st.session_state.chat_history:
    latest_reply = st.session_state.chat_history[-1][1]
    if "GPT" in st.session_state.chat_history[-1][0]:
        tts = gTTS(text=latest_reply, lang='ur')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")
