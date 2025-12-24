import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

INDEX_NAME = "medical-chatbot"
EMBEDDING_DIM = 384
TOP_K = 2
MAX_CONTEXT_CHARS = 3000

assert PINECONE_API_KEY, "Missing PINECONE_API_KEY"
assert GEMINI_API_KEY, "Missing GOOGLE_API_KEY"
