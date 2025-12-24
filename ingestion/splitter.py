# Split the documents into smaller chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )

    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk
