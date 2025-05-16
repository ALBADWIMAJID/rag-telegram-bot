# 🤖 RAG Telegram Bot

A lightweight, production-ready Telegram bot powered by **Retrieval-Augmented Generation (RAG)** pipeline using:
- 🗂 **ChromaDB** for local document retrieval.
- 💡 **OpenAI GPT (Chat Completions API)** for natural language generation.
- 🌐 **Serper API** for real-time web search fallback.

This bot allows users to ask questions via Telegram and get smart, contextualized answers using both your private knowledge base (ChromaDB) and live Google search.



## 💬 Try the Bot

You can try the bot directly on Telegram by clicking the link below:

[👉 Open ClientSupportBot on Telegram](https://t.me/Client_Supportt_Bot)

---

## 🚀 Features

✅ Retrieval-augmented generation (RAG) pipeline.  
✅ Uses **ChromaDB** for vector retrieval.  
✅ Uses **OpenAI ChatGPT** for response generation.  
✅ Uses **Serper API** for live web search integration.  
✅ Ready for deployment on **Railway / Render / Heroku**.  
✅ Safe API key management using environment variables.  

---

## 📁 Project Structure

rag-telegram-bot/

├── client_support_output/

│ └── text/ # Text files to be embedded into ChromaDB

│ └── prepare_chroma_from_txt.py # Script to prepare ChromaDB from text

├── bot_rag_chroma.py # Main Telegram bot code

├── requirements.txt # Python dependencies

├── Procfile # Railway deployment file (worker mode)

├── .env.example # Environment variable template


---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ALBADWIMAJID/rag-telegram-bot.git
cd rag-telegram-bot
2. Configure Environment Variables
Create your .env file by copying from .env.example and replacing the placeholders:


OPENAI_API_KEY=sk-...
TELEGRAM_TOKEN=your_telegram_bot_token_here
SERPER_API_KEY=your_serper_api_key_here
3. Prepare ChromaDB (Optional if using your own documents)
Put your .txt files inside client_support_output/text/ then run:



python prepare_chroma_from_txt.py
This will generate the ChromaDB folder ./chroma_db.

▶️ Run the Bot Locally



python bot_rag_chroma.py
☁️ Deploy to Railway
Push your code to GitHub (do not include real secrets; use .env.example).

Create a new project in Railway.

Connect your GitHub repository.

Go to Variables tab and add:

OPENAI_API_KEY

TELEGRAM_TOKEN

SERPER_API_KEY

Ensure your bot runs as a worker using the Procfile:


worker: python bot_rag_chroma.py
Click Deploy.

🔒 Security Notice
Always use environment variables.

Do not hardcode or push secrets to GitHub.

Use .gitignore to avoid uploading sensitive files.

👷 Requirements
Python 3.9+
Install dependencies:


pip install -r requirements.txt
💡 Technologies Used
ChromaDB

LangChain

OpenAI GPT

Serper API

python-telegram-bot

📚 Usage Examples
Ask the bot questions like:

How do I reset my Steam account password?

How to enable 2FA in Discord?

How do I recover my Netflix account?

The bot will retrieve relevant data from your private knowledge base and supplement it with real-time Google search.

📄 License
MIT License

👤 Author
Made with ❤️ by Majid Albadwi

For demo & academic use.
