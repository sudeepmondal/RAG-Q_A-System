# retriever.py
# User er query r sathe similar document chunks khoje ane

def get_retriever(vector_store, k=3):
    """
    Top-k similar chunks return korbe.
    k=3 mane 3ta best matching chunk ane.
    """
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    return retriever


def retrieve_chunks(retriever, query):
    """Query er jonno relevant chunks fetch koro."""
    docs = retriever.invoke(query)   # Updated method (get_relevant_documents deprecated)
    return docs