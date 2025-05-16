# RAG Telegram Bot 🤖 (ChromaDB + OpenAI + Serper API)

A lightweight Telegram bot that uses RAG (Retrieval-Augmented Generation) pipeline powered by:
- 🗂 ChromaDB (local or cloud via Supabase Storage)
- 💡 OpenAI GPT (Chat Completions API)
- 🌐 Serper API (Google search results as fallback)

---

## Features
- Custom RAG pipeline combining **ChromaDB embeddings** and **Live Web search (Serper API)**.
- Telegram bot interface via **python-telegram-bot**.
- Deployable on **Railway, Render, Heroku, etc.**
- Full separation of API keys using environment variables for security.

---

## Project Structure

```bash
📁 client_support_output/
 └── text/               # Prepared text files for ChromaDB embedding
 └── prepare_chroma_from_txt.py  # Script to prepare and persist ChromaDB from TXT
 └── bot_rag_chroma.py    # Main Telegram Bot RAG logic
 └── requirements.txt
 └── Procfile             # For Railway Deployment
 └── .env.example         # Example of required secrets

Setup Instructions
1. Clone the repository

git clone https://github.com/ALBADWIMAJID/rag-telegram-bot.git
cd rag-telegram-bot
2. Prepare .env file
Create a .env file using the provided .env.example template:


OPENAI_API_KEY=your_openai_api_key_here
TELEGRAM_TOKEN=your_telegram_bot_token_here
SERPER_API_KEY=your_serper_api_key_here
3. Prepare ChromaDB from your text files
Ensure you have your .txt files in client_support_output/text/, then run:


python prepare_chroma_from_txt.py
This will create a persistent ChromaDB at ./chroma_db.

Running the bot locally

python bot_rag_chroma.py
Deployment (Railway Example)
Push your repo to GitHub (without secrets, only .env.example).

Create project in Railway.

Link your repo.

In Railway Variables, add your actual:

OPENAI_API_KEY

TELEGRAM_TOKEN

SERPER_API_KEY

Ensure your bot runs as worker service using:

Railway auto-detects your Procfile.

Example Procfile:



worker: python bot_rag_chroma.py
Deploy.

Notes
You can switch ChromaDB to use Supabase Storage by modifying prepare_chroma_from_txt.py.

This project currently uses langchain-chroma, langchain-openai, and python-telegram-bot.

Make sure to never push your API keys to GitHub (always use .env & Railway Variables).

License
MIT License.

Credits
Created by Majid Albadwi
This bot was built as part of a dialog systems project, combining modern retrieval and generation pipelines.

yaml
Copy
Edit
