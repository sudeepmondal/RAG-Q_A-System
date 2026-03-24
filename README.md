# 📚 RAG Question Answering System

A fully local, production-ready **Retrieval-Augmented Generation (RAG)** system that answers questions based on your own documents (PDF & TXT). Built with LangChain, FAISS, HuggingFace Embeddings, and powered by **Groq's free Llama 3 API**.

> 🔥 No paid API. No cloud database. Runs 100% on your machine.

---

## ✨ Features

- 📄 Upload your own **PDF and TXT** documents
- 🔍 Smart **semantic search** using FAISS vector database
- 🤖 Intelligent answers powered by **Llama 3 (via Groq — free)**
- 🧠 **HuggingFace embeddings** (all-MiniLM-L6-v2) — no API key needed
- ⚡ **Cached pipeline** — models load only once per session
- 🖥️ Clean **Streamlit web UI** — no coding needed to use
- 💾 **Persistent FAISS index** — no re-processing on restart

---

## 🖼️ Demo

```
User: What is machine learning?

Answer: Machine learning is a subset of Artificial Intelligence (AI) 
that allows systems to automatically learn and improve from experience 
without being explicitly programmed. It focuses on developing programs 
that can access data and use it to learn for themselves.

Retrieved Context:
  Chunk 1 — sample1.txt
  Chunk 2 — sample1.txt
```

---

## 🏗️ Project Structure

```
rag_project/
│
├── 📁 data/                  # Put your PDF and TXT files here
│   ├── sample1.txt           # AI & Machine Learning info
│   ├── sample2.txt           # Python programming info
│   └── sample3.txt           # LangChain & RAG info
│
├── 📁 faiss_index/           # Auto-generated vector index (do not edit)
│
├── app.py                    # Streamlit UI — main entry point
├── rag_pipeline.py           # Orchestrates the full RAG pipeline
├── loader.py                 # Loads and splits PDF/TXT documents
├── embedder.py               # HuggingFace embedding model
├── vector_store.py           # FAISS vector store (save/load)
├── retriever.py              # Similarity search — finds top 3 chunks
├── generator.py              # Groq Llama 3 answer generation
├── utils.py                  # Validation, formatting, caching helpers
└── requirements.txt          # Python dependencies
```

---

## ⚙️ How It Works

```
Your Documents (PDF/TXT)
        │
        ▼
  [loader.py] Load & Split into chunks (500 chars, 50 overlap)
        │
        ▼
  [embedder.py] Convert chunks → vectors (all-MiniLM-L6-v2)
        │
        ▼
  [vector_store.py] Store vectors in FAISS index (saved locally)
        │
   User asks a question
        │
        ▼
  [retriever.py] Find top 3 most similar chunks
        │
        ▼
  [generator.py] Send context + question → Groq Llama 3
        │
        ▼
  💡 Final Answer displayed in Streamlit UI
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.11** (64-bit) — [Download here](https://www.python.org/downloads/release/python-3119/)
- A free **Groq API key** — [Get it here](https://console.groq.com)

---

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag_project.git
cd rag_project
```

---

### 2. Create Virtual Environment

```bash
# Create venv with Python 3.11
py -3.11 -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4. Get Your Free Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for free (Google login works)
3. Click **"API Keys"** → **"Create API Key"**
4. Copy your key (looks like: `gsk_xxxxxxxxxxxxxxxxxxxx`)

---

### 5. Add Your API Key

Open `generator.py` and replace line 8:

```python
# Before
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxx"

# After
GROQ_API_KEY = "gsk_your_actual_key_here"
```

---

### 6. Add Your Documents

Drop any `.pdf` or `.txt` files into the `data/` folder.

> 3 sample documents are already included to test with.

---

### 7. Run the App

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501** and start asking questions! 🎉

---

## 📦 Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | LangChain 0.2.16 |
| LLM | Groq — Llama 3.3 70B (Free) |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| Vector Database | FAISS (local) |
| UI | Streamlit |
| PDF Loader | PyPDF |
| Language | Python 3.11 |

---

## 🔧 Adding New Documents

1. Copy your `.pdf` or `.txt` files into the `data/` folder
2. Delete the old FAISS index:

```bash
# Windows
rmdir /s /q faiss_index

# Mac/Linux
rm -rf faiss_index
```

3. Restart the app:

```bash
streamlit run app.py
```

The system will automatically rebuild the index with your new documents.

---

## 🛠️ Troubleshooting

| Problem | Solution |
|--------|----------|
| `ModuleNotFoundError` | Make sure venv is active and run `pip install -r requirements.txt` |
| `API Key error` | Check your Groq API key in `generator.py` |
| `No documents found` | Add `.pdf` or `.txt` files to the `data/` folder |
| `Model decommissioned` | Update model name in `generator.py` — check [Groq docs](https://console.groq.com/docs/deprecations) |
| Answer says "could not find" | Make sure your question matches the document content |
| Slow first run | Normal — embedding model (~80MB) downloads once and caches |

---

## 🌱 Future Improvements

- [ ] Support for `.docx` Word documents
- [ ] Multi-language document support
- [ ] Chat history / conversation memory
- [ ] Upload documents directly from the UI
- [ ] Docker support for easy deployment
- [ ] Support for multiple vector stores (Chroma, Pinecone)

---


## 🙋‍♂️ Author

Made with ❤️ by **[Your Name]**

- GitHub: [@sudeepmondal](https://github.com/sudeepmondal)
- LinkedIn: [smdeep](https://linkedin.com/in/smdeep)

---

## ⭐ Support

If you found this project helpful, please give it a **star** on GitHub! It helps others find it too.

```
git clone → pip install → add API key → streamlit run app.py → done! 🚀
```