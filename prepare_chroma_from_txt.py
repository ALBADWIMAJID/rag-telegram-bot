import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from fsspec.implementations.s3 import S3FileSystem

# Read environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = "rag-chromadb"

# Setup S3 filesystem using fsspec
fs = S3FileSystem(key=AWS_ACCESS_KEY_ID, secret=AWS_SECRET_ACCESS_KEY)

# Your S3 folder path
S3_PERSIST_DIR = f"s3://{S3_BUCKET}/chroma_db/"

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
documents = []

TEXT_DIRECTORY = "./text"
for filename in os.listdir(TEXT_DIRECTORY):
    if filename.endswith(".txt"):
        filepath = os.path.join(TEXT_DIRECTORY, filename)
        loader = TextLoader(filepath, encoding="utf-8")
        docs = loader.load()
        documents.extend(docs)

# Persist to S3
db = Chroma.from_documents(documents, embedding, persist_directory=S3_PERSIST_DIR, filesystem=fs)

print(f"✅ تم تحميل جميع الملفات إلى ChromaDB على {S3_PERSIST_DIR}")
