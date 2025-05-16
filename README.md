
# 🤖 RAG Telegram Bot

A lightweight, production-ready Telegram bot powered by **Retrieval-Augmented Generation (RAG)** pipeline using:
- 🗂 **ChromaDB** for local document retrieval.
- 💡 **OpenAI GPT (Chat Completions API)** for natural language generation.
- 🌐 **Serper API** for real-time web search fallback.

This bot allows users to ask questions via Telegram and get smart, contextualized answers using both your **private knowledge base (ChromaDB)** and **live Google search**.

---

## 💬 Try the Bot

You can try the bot directly on Telegram by clicking the link below:

[👉 Open ClientSupportBot on Telegram](https://t.me/Client_Supportt_Bot)

---

## 🚀 Features

✅ Retrieval-Augmented Generation (RAG) pipeline  
✅ Uses **ChromaDB** for vector retrieval  
✅ Uses **OpenAI ChatGPT** for response generation  
✅ Uses **Serper API** for live web search integration  
✅ Ready for deployment on **Railway / Render / Heroku**  
✅ Secure API key management using `.env` file  

---

## 📁 Project Structure

```
rag-telegram-bot/
├── client_support_output/
│   └── text/                 # Text files to be embedded into ChromaDB
│   └── prepare_chroma_from_txt.py  # Script to prepare ChromaDB from text files
├── bot_rag_chroma.py          # Main Telegram bot code
├── requirements.txt           # Python dependencies
├── Procfile                   # For Railway deployment (worker mode)
├── .env.example               # Environment variable template
```

---

## 🔧 Setup Instructions

### 💻 How to run this Bot locally (Windows / Mac / Linux)

#### ✅ Step 1: Clone the repository
```bash
git clone https://github.com/ALBADWIMAJID/rag-telegram-bot.git
cd rag-telegram-bot
```

#### ✅ Step 2: Create and activate a virtual environment
##### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
##### On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### ✅ Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

#### ✅ Step 4: Prepare ChromaDB from your `.txt` documents
1. Place your `.txt` files inside `client_support_output/text/`
2. Run:
```bash
python prepare_chroma_from_txt.py
```

#### ✅ Step 5: Setup your `.env` file
1. Copy `.env.example` to `.env`
2. Fill it with your credentials:
```
OPENAI_API_KEY=your_openai_api_key_here
TELEGRAM_TOKEN=your_telegram_bot_token_here
SERPER_API_KEY=your_serper_api_key_here
```

#### ✅ Step 6: Run the bot locally
```bash
python bot_rag_chroma.py
```

---

## 💡 How to test the bot

1. Open Telegram and search for your bot.
2. Send any question, like:
    - `How do I reset my Steam password?`
    - `How to enable 2FA in Discord?`
3. The bot will answer from ChromaDB and Google search via Serper API.

---

## ⚠ Notes for local run
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```
- You can always add new `.txt` files and re-run `prepare_chroma_from_txt.py`.
- Ensure `.env` is correctly configured.

---

## ☁️ Deployment to Railway (24/7 Hosting)

#### 1. Push your code to GitHub (ensure **no secrets** are hardcoded)
```bash
git add .
git commit -m "Clean RAG Telegram Bot safe version"
git push
```

#### 2. On Railway:
- Create a new **project**.
- Connect your **GitHub repository**.
- Go to **Variables**, and add:
```
OPENAI_API_KEY
TELEGRAM_TOKEN
SERPER_API_KEY
```

#### 3. Ensure your `Procfile` is correct:
```
worker: python bot_rag_chroma.py
```

#### 4. Click **Deploy**.

---

## 🔒 Security Notice
- Always use environment variables (`.env`).
- Do not hardcode or push secrets to GitHub.
- Use `.gitignore` to avoid uploading sensitive files.

---

## 👷 Requirements
- Python 3.9+
- Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 💡 Technologies Used
- ChromaDB
- LangChain
- OpenAI GPT (Chat Completions API)
- Serper API
- Python Telegram Bot

---

## 📚 Usage Examples
- `How do I reset my Discord password?`
- `How to recover my Netflix account?`
- `How to set up Gmail in Outlook?`

---

## 📄 License
MIT License

---

## 👤 Author
Made with  by **Majid Albadwi**  
For demonstration & academic use only.
