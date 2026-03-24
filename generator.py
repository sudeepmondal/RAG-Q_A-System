# generator.py
# Groq API use kore free Llama 3 model diye answer generate kore
# No local model download needed!

from groq import Groq

# ============================================
# TOMAR GROQ API KEY EKHANE BOSAO
GROQ_API_KEY = "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"
# ============================================

_client = None

def load_generator():
    """Groq client initialize koro — only once per session."""
    global _client
    
    if _client is None:
        if not GROQ_API_KEY or GROQ_API_KEY == "gsk_xxxxxxxxxxxxxxxxxxxx":
            raise ValueError(
                "Groq API key set koro nai! "
                "generator.py file e GROQ_API_KEY variable e tomar key bosao."
            )
        _client = Groq(api_key=GROQ_API_KEY)
        print("Groq client ready! (Llama 3 model use hobe)")
    
    return _client


def generate_answer(query, context_docs):
    """
    Retrieved context + user query combine kore
    Groq er Llama 3 model diye answer generate koro.
    """
    client = load_generator()
    
    # Sob retrieved chunks ek sathe join koro
    context = "\n\n".join([doc.page_content for doc in context_docs])
    
    # Llama 3 ke system + user message pathao
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # Free Llama 3 model (8B parameters)
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Answer questions based ONLY on the provided context. "
                    "Give complete, clear, and detailed answers. "
                    "If the answer is not in the context, say: "
                    "'I could not find this information in the provided documents.'"
                )
            },
            {
                "role": "user",
                "content": (
                    f"Context:\n{context}\n\n"
                    f"Question: {query}\n\n"
                    f"Answer:"
                )
            }
        ],
        temperature=0.1,      # Low temperature = more factual answers
        max_tokens=512        # Maximum answer length
    )
    
    answer = response.choices[0].message.content.strip()
    return answer