#  Personal Finance RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from the **"Personal Finance for Students"** PDF using semantic search and a language model.

Built with:
-  LangChain
-  ChromaDB
-  Hugging Face Transformers (FLAN-T5)
-  Gradio for web UI
-  PDF as knowledge source

---

##  Features

-  Upload and process a PDF
-  Retrieve relevant content with vector search
-  Answer questions using FLAN-T5
-  Chatbot UI with Gradio

---

##  RAG Flow

```mermaid
graph TD
    A[User Question] --> B[Retriever (ChromaDB)]
    B --> C[Relevant Chunks]
    C --> D[Generator (Flan-T5)]
    D --> E[Final Answer]

---

 Preview

 Project Structure

 fin-rag/
├── data/                      # PDF files
│   └── personal_finance_for_students.pdf
├── rag/                       # Core logic
│   ├── __init__.py
│   ├── pdf_reader.py
│   ├── text_chunker.py
│   ├── embed_store.py
│   └── retriever_generator.py
├── chroma_store/              # Persistent vector store
├── app.py                     # CLI-based interaction
├── rag_ui.py                  # Gradio web app
└── README.md

---

Installation

git clone https://github.com/your-username/fin-rag.git
cd fin-rag

pip install -r requirements.txt

---

How to Run

🔹 CLI Mode

python app.py

🔹 Gradio UI

python rag_ui.py

---

Tech Stack

| Category            | Technology / Tool                                   | Purpose                                       |
| ------------------- | --------------------------------------------------- | --------------------------------------------- |
| **Programming**     | Python                                              | Core language for the RAG pipeline            |
| **LLM Framework**   | LangChain (`langchain`, `langchain-community`)      | Framework for Retrieval-Augmented Generation  |
| **Embeddings**      | `sentence-transformers` (`all-MiniLM-L6-v2`)        | For converting text to vector representations |
| **Vector Store**    | ChromaDB (`chromadb`)                               | To store and retrieve vectorized chunks       |
| **PDF Parsing**     | PyMuPDF (`pymupdf`)                                 | Extract text from PDF files                   |
| **Model Inference** | Hugging Face Transformers (`transformers`, `torch`) | Load and run text generation models           |
| **Frontend**        | Gradio                                              | Interactive web UI to ask questions           |
| **Environment**     | Python virtual environment                          | Isolated setup for dependencies               |
| **Version Control** | Git + GitHub                                        | Code management and collaboration             |


