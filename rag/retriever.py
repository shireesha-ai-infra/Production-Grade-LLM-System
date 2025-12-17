def retrieve(query_embedding, index, docs, top_k=5):
    distances, indices = index.search(query_embedding, top_k)
    return [docs[i] for i in indices[0]]