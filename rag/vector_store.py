import os
import faiss
import pickle

from rag.dataset_loader import load_dataset
from rag.create_embeddings import generate_embeddings


def build_vector_store():

    # Create folder automatically
    os.makedirs("vectordb", exist_ok=True)

    df = load_dataset()

    documents = df["content"].tolist()

    embeddings = generate_embeddings(documents)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, "vectordb/news.index")

    with open("vectordb/documents.pkl", "wb") as f:
        pickle.dump(documents, f)

    print("✅ Vector database created successfully")


if __name__ == "__main__":
    build_vector_store()