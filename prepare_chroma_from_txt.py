from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TEXT_DIRECTORY = r"C:\Users\albad\Desktop\my works\мои работы в 6 семестр\Диалоговые системы\chatbot telegram\client_support_output\text"

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
documents = []

for filename in os.listdir(TEXT_DIRECTORY):
    if filename.endswith(".txt"):
        filepath = os.path.join(TEXT_DIRECTORY, filename)
        loader = TextLoader(filepath, encoding="utf-8")  # إجبار الترميز على UTF-8
        try:
            docs = loader.load()
            documents.extend(docs)
            print(f"تم تحميل: {filename}")
        except Exception as e:
            print(f"❌ خطأ أثناء تحميل {filename}: {e}")

db = Chroma.from_documents(
    documents, embedding, persist_directory="./chroma_db"
)

print("✅ تم تحميل جميع الملفات إلى ChromaDB وحفظها بنجاح في ./chroma_db")
