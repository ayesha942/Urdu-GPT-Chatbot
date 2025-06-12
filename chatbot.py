import openai
import os
from dotenv import load_dotenv

# Load secret API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Intro message
print("🤖 Urdu GPT CLI Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("🧕🏻 Tum: ")
    if user_input.lower() == "exit":
        print("👋 Khuda Hafiz!")
        break

    try:
        # Send message to GPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tum ek intelligent Urdu chatbot ho. Hamesha Urdu mein jawab do."},
                {"role": "user", "content": user_input}
            ]
        )

        # Print reply
        reply = response['choices'][0]['message']['content']
        print("🤖 GPT:", reply)

    except Exception as e:
        print("❌ Error:", e)
