from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os
import openai
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ---------------- Secure Configuration ----------------
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
CHROMA_DB_URL = os.getenv("CHROMA_DB_URL")  # ⭐ الآن نحمل Chroma من Supabase URL
# ------------------------------------------------------

# Initialize OpenAI Client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Custom Chroma retriever that works from remote Supabase SQLite file
def get_chroma_from_supabase(url):
    local_file = "./chroma_db.sqlite3"
    if not os.path.exists(local_file):
        print("⬇ Downloading ChromaDB from Supabase...")
        response = requests.get(url)
        with open(local_file, "wb") as f:
            f.write(response.content)
        print("✅ Download complete.")
    else:
        print("✅ ChromaDB already exists locally, using cache.")
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    db = Chroma(persist_directory=".", embedding_function=embeddings)
    return db.as_retriever()

retriever = get_chroma_from_supabase(CHROMA_DB_URL)

# Web Search using Serper API
def web_search(query):
    headers = {"X-API-KEY": SERPER_API_KEY}
    payload = {"q": query}
    try:
        response = requests.post("https://google.serper.dev/search", headers=headers, json=payload)
        results = response.json()
        snippets = []
        if 'organic' in results:
            for item in results['organic'][:3]:
                title = item.get('title', 'No title')
                snippet = item.get('snippet', 'No snippet')
                link = item.get('link', '')
                snippets.append(f"🔗 {title}\n{snippet}\n{link}")
        return "\n\n".join(snippets)
    except Exception as e:
        return f"❌ Web search failed: {e}"

# Combined RAG Pipeline (ChromaDB + Web)
def custom_rag_pipeline(question):
    docs = retriever.invoke(question)
    chroma_text = "\n\n".join([f"[Chroma snippet {i+1}]: {doc.page_content[:500]}" for i, doc in enumerate(docs)]) if docs else "No relevant documents found in ChromaDB."
    chroma_sources = [f"- Chroma snippet {i+1}" for i in range(len(docs))] if docs else ["- No ChromaDB source found"]

    web_results = web_search(question)
    web_source = "- Web Search (Serper API results included)" if web_results.strip() else "- No web results found"

    prompt = f"""
Question: {question}

Knowledge Base Results:
{chroma_text}

Internet Results:
{web_results}

Please provide a professional, helpful, and accurate answer using the provided knowledge base and internet results.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        sources_info = "\n\n📚 Sources Used:\n" + "\n".join(chroma_sources) + "\n" + web_source
        return answer + sources_info
    except Exception as e:
        return f"❌ Error generating answer from OpenAI: {e}"

# Telegram Bot Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Hello! I'm your support assistant bot. You can ask me any question.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text("🔎 Please wait... processing your request...")
    try:
        answer = custom_rag_pipeline(user_message)
        await update.message.reply_text(answer)
    except Exception as e:
        await update.message.reply_text(f"❌ An error occurred while processing your request: {e}")

# Bot Initialization
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 Professional RAG Chroma Bot is running...")
app.run_polling()
