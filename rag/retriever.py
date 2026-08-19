import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

index = faiss.read_index("vectordb/news.index")

with open("vectordb/documents.pkl", "rb") as f:
    documents = pickle.load(f)


def retrieve_documents(query, top_k=10):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(documents[idx])

    return results