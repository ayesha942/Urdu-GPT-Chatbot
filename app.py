# app.py
import streamlit as st
from chat_engine import get_urdu_reply

st.set_page_config(page_title="🤖 Urdu Gemini Chatbot")

st.title("🤖 Urdu Gemini Chatbot")
st.markdown("Talk to your AI in **Urdu** 🕌")

# Chat history using Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("🧕🏻 Sawal likhein...")

if user_input:
    reply = get_urdu_reply(user_input)
    st.session_state.chat_history.append(("🧕🏻 Tum", user_input))
    st.session_state.chat_history.append(("🤖 GPT", reply))

# Display chat history
for role, msg in st.session_state.chat_history:
    with st.chat_message("user" if "Tum" in role else "assistant"):
        st.markdown(msg)
