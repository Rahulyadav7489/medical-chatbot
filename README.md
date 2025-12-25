# 🩺 Medical Chatbot (RAG-Based)

A web-based Medical Question-Answering Chatbot** built using Retrieval-Augmented Generation (RAG)**.  
The chatbot answers medical queries using a custom knowledge base and avoids hallucinations by responding only from retrieved context.

---

## 🚀 Features

- Chat-style web interface  
- Context-aware medical answers  
- Semantic search using vector embeddings  
- Medical-safe responses (no guessing)  
- Fast and lightweight LLM inference  

---

## 🛠️ Tech Stack

- Backend:** Flask (Python)
- LLM:** Google Gemini (gemini-flash-lite-latest)
- Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
- Vector Database:** Pinecone
- Frontend:** HTML, CSS, JavaScript
- Python Version:** 3.9+

---



Setup:

1. git clone "https://github.com/Rahulyadav7489/medical-chatbot" 
2. python -m venv venv  
3. activate venv  
4. pip install -r requirements.txt  
5. Set environment variables:  
   GEMINI_API_KEY=your_key  
   PINECONE_API_KEY=your_key  
6. python app.py  
7. Open http://127.0.0.1:5000 in browser  

🧠 How It Works

User enters a medical question in the chatbot UI
The query is converted into embeddings
Relevant documents are retrieved from Pinecone
Retrieved context is sent to the Gemini LLM
The chatbot generates a response using only retrieved information



⚠️ Medical Disclaimer

This chatbot is for educational purposes only.
It is not a substitute for professional medical advice, diagnosis, or treatment.




🚀 Future Improvements

imporve knowledgebase
Source citations in responses
Confidence scoring
Voice input support
Cloud deployment

571182111334.dkr.ecr.eu-north-1.amazonaws.com/medicare

👤 Author
Rahul Yadav
B.Tech (AI/ML) Student
Aspiring AI Engineer


📄 License
This project is licensed under the MIT License.