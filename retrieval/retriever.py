from vector_store import index, pc
from ingestion import embedding
top_k=5

def retrieve_context(query):
    query_vector = embedding.embed_query(query)

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    contexts = []
    for match in results["matches"]:
        text = match["metadata"].get("text")
        if text:
            contexts.append(text)

    return "\n\n".join(contexts)
