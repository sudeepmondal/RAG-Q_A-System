# loader.py
# PDF and TXT files load kore data/ folder theke
# Documents ke chunks e split kore

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


def load_documents(data_dir="data"):
    """data/ folder er sob PDF and TXT files load koro."""
    documents = []
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"'{data_dir}/' folder create kora hoyeche.")
        return documents
    
    files = os.listdir(data_dir)
    
    if not files:
        print(f"'{data_dir}/' folder e kono file nei!")
        return documents
    
    for filename in files:
        filepath = os.path.join(data_dir, filename)
        
        try:
            if filename.endswith(".pdf"):
                loader = PyPDFLoader(filepath)
                documents.extend(loader.load())
                print(f"Loaded PDF: {filename}")
                
            elif filename.endswith(".txt"):
                loader = TextLoader(filepath, encoding="utf-8")
                documents.extend(loader.load())
                print(f"Loaded TXT: {filename}")
                
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            continue
    
    print(f"Total documents loaded: {len(documents)}")
    return documents


def split_documents(documents, chunk_size=500, chunk_overlap=50):
    """Documents ke 500 character er chunks e split koro."""
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    
    chunks = splitter.split_documents(documents)
    print(f"Total chunks created: {len(chunks)}")
    return chunks