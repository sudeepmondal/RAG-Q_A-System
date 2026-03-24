# rag_pipeline.py
# Sob modules ke connect kore complete pipeline banay

from loader import load_documents, split_documents
from embedder import get_embeddings
from vector_store import create_vector_store, load_vector_store
from retriever import get_retriever, retrieve_chunks
from generator import generate_answer


def build_pipeline():
    """
    RAG pipeline build koro:
    - First run: documents load → chunks → embeddings → FAISS index save
    - Later runs: saved FAISS index load (fast)
    """
    print("=== RAG Pipeline Building ===")
    
    # Step 1: Embedding model load
    embeddings = get_embeddings()
    
    # Step 2: Existing vector store load korar try
    vector_store = load_vector_store(embeddings)
    
    if vector_store is None:
        print("No existing index. Building from documents...")
        
        documents = load_documents("data")
        
        if not documents:
            raise ValueError(
                "data/ folder e kono document nei! "
                "PDF ba TXT file add koro."
            )
        
        chunks = split_documents(documents)
        vector_store = create_vector_store(chunks, embeddings)
    
    # Step 3: Retriever ready
    retriever = get_retriever(vector_store, k=3)
    
    print("=== Pipeline Ready! ===\n")
    return retriever


def ask(retriever, query):
    """
    Complete RAG flow:
    1. Query → relevant chunks retrieve
    2. Chunks + Query → Groq Llama 3 → Answer
    """
    context_docs = retrieve_chunks(retriever, query)
    answer = generate_answer(query, context_docs)
    return answer, context_docs