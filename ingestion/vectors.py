import uuid
from .embeddings import embedding

def convert_to_vectors(text_chunks):
    vectors = []
    for doc in text_chunks:
        vectors.append({
            "id": str(uuid.uuid4()),
            "values": embedding.embed_query(doc.page_content),
            "metadata": {
                "source": doc.metadata.get("source"),
                "text": doc.page_content   
            }
        })
