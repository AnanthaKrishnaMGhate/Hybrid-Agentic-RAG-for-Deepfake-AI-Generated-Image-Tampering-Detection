from rag.rag_pipeline import run_rag

query = """
is tommorow 13/08/2026 karnataka bandh

"""

result = run_rag(query)

print(result)