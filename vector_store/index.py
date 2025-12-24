from pinecone import Pinecone
from config import PINECONE_API_KEY
from config import INDEX_NAME

pc= Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)
