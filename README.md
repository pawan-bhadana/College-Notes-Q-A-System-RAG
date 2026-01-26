# 📘 College Notes Q&A System (RAG) — Ongoing

This project is a **Retrieval-Augmented Generation (RAG) based Question & Answer system** that allows students to ask questions over their **college notes, lecture PDFs, and study material** and receive accurate, context-aware answers.

Instead of relying only on a language model’s internal knowledge, the system **retrieves relevant content from the notes first** and then generates answers grounded in that retrieved information.

---

## 🚀 What This Project Does

- Takes **college notes / PDFs** as input  
- Splits documents into smaller **text chunks**  
- Converts chunks into **semantic embeddings**  
- Stores embeddings in a **vector database**  
- For each question:
  - Retrieves the **most relevant note sections**
  - Feeds them to an **LLM** to generate grounded answers  

This approach helps reduce hallucinations and ensures answers are based on actual study material.

---

## 🧠 Why Retrieval-Augmented Generation (RAG)?

Large Language Models cannot directly read or remember new documents.  
RAG solves this by:

- Retrieving relevant information from external documents  
- Injecting it into the model’s context before answering  

This makes the system more **accurate, reliable, and explainable**, especially for academic use cases.

---

## 🛠️ Tech Stack

- **Python**
- **Embeddings Model** (all-MiniLM-L6-v2)
- **Vector Database** (FAISS)
- **LLM** (OpenAI GPT)

---

## 📂 Project Workflow

1. Load and preprocess college notes / PDFs  
2. Split documents into manageable chunks  
3. Generate embeddings for each chunk  
4. Store embeddings in a vector database  
5. Convert user queries into embeddings  
6. Retrieve top relevant chunks using cosine similarity  
7. Generate answers using the retrieved context  

---

## 🎯 Use Cases

- Studying for exams  
- Quick revision of lecture notes  
- Understanding topics from large PDFs  
- Academic document Q&A  

---

## 📌 Note

This project is **actively being developed** as a learning-focused project to explore practical applications of **RAG, embeddings, and large language models**.
