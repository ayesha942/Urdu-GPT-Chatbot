import os
import google.generativeai as genai
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

# Load Gemini API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat(history=[])

# Init TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice

# Speech recognizer
r = sr.Recognizer()

print("🎤 Urdu GPT Voice Chatbot — Say something or type 'exit' to quit.")

while True:
    try:
        with sr.Microphone() as source:
            print("\n🧕🏻 Tum (Speak now)...")
            audio = r.listen(source, phrase_time_limit=5)
            user_input = r.recognize_google(audio, language="ur-PK")
            print(f"🧕🏻 Tum: {user_input}")
    except sr.UnknownValueError:
        print("❌ Couldn't understand. Try again.")
        continue
    except KeyboardInterrupt:
        break

    if user_input.lower() == "exit":
        print("👋 Khuda Hafiz!")
        break

    try:
        prompt = f"Urdu mein chatbot ban kar jawab dein: {user_input}"
        response = chat.send_message(prompt)
        reply = response.text.strip()
        print("🤖 GPT:", reply)
        engine.say(reply)
        engine.runAndWait()
    except Exception as e:
        print("❌ Error:", e)
