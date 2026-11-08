from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def load_vector_store():
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )


def search_pricing_rules(question: str):
    vector_store = load_vector_store()

    results = vector_store.similarity_search(question, k=3)

    return results
