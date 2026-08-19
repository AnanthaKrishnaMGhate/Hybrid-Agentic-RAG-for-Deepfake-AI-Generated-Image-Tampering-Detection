from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def generate_embeddings(documents):

    # Ensure every document is a string
    documents = [str(doc) for doc in documents]

    embeddings = model.encode(
        documents,
        batch_size=32,
        show_progress_bar=True
    )

    return embeddings