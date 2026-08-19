from rag.retriever import retrieve_documents

results = retrieve_documents(
    " Siddaramayah is  the CM of Karnataka at 2025"
)

for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print(doc[:500])