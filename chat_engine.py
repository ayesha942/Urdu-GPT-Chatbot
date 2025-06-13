import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_urdu_reply(user_input):
    try:
        prompt = f"Urdu mein chatbot ban kar jawab dein: {user_input}"
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"
