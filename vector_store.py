# vector_store.py
# FAISS vector database e embeddings store kore
# Local disk e save/load kore — cloud lagbe na

from langchain_community.vectorstores import FAISS
import os

FAISS_INDEX_PATH = "faiss_index"


def create_vector_store(chunks, embeddings):
    """Chunks theke vectors banao and FAISS e save koro."""
    print("FAISS vector store creating...")
    
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(FAISS_INDEX_PATH)
    
    print(f"Vector store saved to '{FAISS_INDEX_PATH}/'")
    return vector_store


def load_vector_store(embeddings):
    """Disk theke existing FAISS index load koro."""
    
    if not os.path.exists(FAISS_INDEX_PATH):
        return None
    
    print("Existing FAISS index loading...")
    
    vector_store = FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    print("Vector store loaded!")
    return vector_store