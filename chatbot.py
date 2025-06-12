import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure
genai.configure(api_key=api_key)

# Create chat model
model = genai.GenerativeModel("models/gemini-1.5-flash")  

chat = model.start_chat(history=[])

print("🤖 Urdu Gemini CLI Chatbot")
print("Type 'exit' to quit\n")

while True:
    try:
        user_input = input("🧕🏻 Tum: ")
        if user_input.lower() == "exit":
            print("👋 Khuda Hafiz!")
            break
        response = chat.send_message(f"Urdu mein chatbot ban kar jawab dein: {user_input}")
        print("🤖 GPT:", response.text.strip())
    except Exception as e:
        print("❌ Error:", e)
