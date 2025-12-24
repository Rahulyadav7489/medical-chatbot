def batch_upsert(index, vectors, batch_size=50):
    for i in range(0, len(vectors), batch_size):
        index.upsert(vectors=vectors[i:i+batch_size])
        print(f"Upserted {i} → {i+len(vectors[i:i+batch_size])}")

