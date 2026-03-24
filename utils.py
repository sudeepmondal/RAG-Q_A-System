# utils.py
# Helper functions: validation, formatting, caching

import streamlit as st


def validate_query(query):
    """User query valid kina check koro."""
    
    if not query or not query.strip():
        return False, "Please enter a question."
    
    if len(query.strip()) < 3:
        return False, "Question is too short. Please be more specific."
    
    if len(query) > 500:
        return False, "Question is too long. Keep it under 500 characters."
    
    return True, ""


def format_context(docs):
    """Retrieved chunks UI te display er jonno format koro."""
    formatted = []
    
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "Unknown")
        source = source.split("/")[-1].split("\\")[-1]
        
        formatted.append({
            "chunk_number": i,
            "source": source,
            "content": doc.page_content.strip()
        })
    
    return formatted


@st.cache_resource
def get_cached_pipeline():
    """
    Pipeline cache koro — models ekbar e load hobe,
    har bar question korle reload hobe na.
    """
    from rag_pipeline import build_pipeline
    return build_pipeline()