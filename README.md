# 🤖 Urdu-GPT-Chatbot (Gemini-Powered CLI)

An open-source **Urdu-language AI chatbot** that runs in your **command-line interface (CLI)**. It uses **Google Gemini 1.5 Flash (Free Tier)** through the official `google-generativeai` Python SDK.

Perfect for developers, students, or AI enthusiasts who want to learn how to create a native Urdu chatbot using LLMs.

---

## 🌟 Features

- CLI-based Urdu chatbot  
- Uses Google Gemini 1.5 Flash (free & fast)  
- Responds like a fluent Urdu speaker  
- Clean and minimal Python code  
- Secure API setup with `.env`  
- Open-source (MIT) – feel free to extend or fork it

---

## 🧰 Tech Stack

- Python 3.10+  
- Google Gemini API (`google-generativeai`)  
- Virtual Environment (venv)  
- `.env` for API key

---

## 🚀 Setup Instructions

```bash
# 1. Clone the project
git clone https://github.com/yourusername/Urdu-GPT-Chatbot.git
cd Urdu-GPT-Chatbot

# 2. Set up virtual environment
python -m venv venv
venv\Scripts\activate         # On Windows
# or
source venv/bin/activate      # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key in a .env file
echo GEMINI_API_KEY=your_api_key_here > .env

# 5. Run the chatbot
python chatbot.py
