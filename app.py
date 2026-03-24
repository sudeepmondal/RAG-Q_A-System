# app.py
# Streamlit UI — main interface

import streamlit as st
from utils import validate_query, format_context, get_cached_pipeline
from rag_pipeline import ask

# Page setup
st.set_page_config(
    page_title="RAG System",
    page_icon="📚",
    layout="centered"
)

st.title("📚 RAG Question Answering System")
st.markdown("Ask any question based on the documents in the `data/` folder.")
st.divider()

# Pipeline load (cached)
with st.spinner("System loading..."):
    try:
        retriever = get_cached_pipeline()
        st.success("✅ System ready! Powered by Groq Llama 3")
    except ValueError as e:
        st.error(f"❌ Setup Error: {e}")
        st.info("generator.py file e GROQ_API_KEY set koro.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.stop()

# Question input
query = st.text_input(
    "Your question:",
    placeholder="e.g. What is machine learning?",
    max_chars=500
)

col1, col2 = st.columns([1, 4])
with col1:
    submit = st.button("Ask", type="primary", use_container_width=True)
with col2:
    clear = st.button("Clear", use_container_width=True)

if clear:
    st.rerun()

# Answer generate
if submit:
    is_valid, error_msg = validate_query(query)
    
    if not is_valid:
        st.warning(error_msg)
    else:
        with st.spinner("Thinking... (Groq Llama 3)"):
            try:
                answer, context_docs = ask(retriever, query)
                
                # Answer display
                st.subheader("💡 Answer")
                st.write(answer)
                st.divider()
                
                # Context display
                st.subheader("📄 Retrieved Context")
                st.caption("Documents used to generate this answer:")
                
                formatted = format_context(context_docs)
                for chunk in formatted:
                    with st.expander(
                        f"Chunk {chunk['chunk_number']} — {chunk['source']}"
                    ):
                        st.write(chunk["content"])
                        
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Sidebar
with st.sidebar:
    st.header("⚙️ System Info")
    st.markdown("""
    **LLM:** Groq Llama 3 (Free)
    
    **Embeddings:** all-MiniLM-L6-v2
    
    **Vector DB:** FAISS (local)
    
    **How it works:**
    1. Question → vector convert
    2. FAISS e similar chunks search
    3. Context + Question → Llama 3
    4. Complete answer generate
    """)
    
    st.divider()
    
    if st.button("🔄 Rebuild Index"):
        import shutil, os
        if os.path.exists("faiss_index"):
            shutil.rmtree("faiss_index")
            st.cache_resource.clear()
            st.success("Index deleted! Restarting...")
            st.rerun()
    
    st.caption("Free • Local • No paid API")