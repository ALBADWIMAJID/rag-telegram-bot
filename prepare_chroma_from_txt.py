from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# استخدام مجلد مؤقت داخل الحاوية (كل مرة يبدأ نظيف)
PERSIST_DIRECTORY = "/tmp/chroma_db"

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
documents = []

# تحميل كل ملفات TXT داخل مشروعك (في مجلد ثابت)
TEXT_DIRECTORY = "./text"  # يجب أن تضع الملفات هنا داخل مشروعك قبل الـ build

for filename in os.listdir(TEXT_DIRECTORY):
    if filename.endswith(".txt"):
        filepath = os.path.join(TEXT_DIRECTORY, filename)
        loader = TextLoader(filepath, encoding="utf-8")
        try:
            docs = loader.load()
            documents.extend(docs)
            print(f"تم تحميل: {filename}")
        except Exception as e:
            print(f"❌ خطأ أثناء تحميل {filename}: {e}")

# إنشاء قاعدة بيانات مؤقتة كل مرة يعمل البوت
db = Chroma.from_documents(
    documents, embedding, persist_directory=PERSIST_DIRECTORY
)

print(f"✅ تم تحميل جميع الملفات ({len(documents)}) إلى ChromaDB في {PERSIST_DIRECTORY}")
