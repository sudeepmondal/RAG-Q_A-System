# embedder.py
# HuggingFace free embedding model use kore
# Text ke numbers (vectors) e convert kore

from langchain_huggingface import HuggingFaceEmbeddings


def get_embeddings():
    """
    HuggingFace embedding model load koro.
    First run e ~80MB download hobe — পরে cache theke load hobe.
    """
    print("Embedding model loading...")
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    
    print("Embedding model ready!")
    return embeddings