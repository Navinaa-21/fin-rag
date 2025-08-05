#  Personal Finance RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot that answers questions from the **"Personal Finance for Students"** PDF using semantic search and a language model.

---

##  Built With

-  LangChain  
-  ChromaDB  
-  Hugging Face Transformers (FLAN-T5)  
-  Gradio (for web UI)  
-  PyMuPDF (PDF as knowledge source)

---

##  Features

- Upload and process a PDF file  
- Perform semantic search with ChromaDB  
- Use `all-MiniLM-L6-v2` embeddings for chunk matching  
- Generate answers with `Flan-T5`  
- Chatbot UI with Gradio

---

##  Project Structure

```
fin-rag/
├── data/                      # PDF files
│   └── personal_finance_for_students.pdf
├── rag/                       # Core logic
│   ├── __init__.py
│   ├── pdf_reader.py          # Read and extract PDF text
│   ├── text_chunker.py        # Split text into chunks
│   ├── embed_store.py         # Generate embeddings & store in ChromaDB
│   └── retriever_generator.py # Retrieve chunks & generate answers
├── chroma_store/              # Persistent vector store (ChromaDB)
├── app.py                     # CLI-based interaction
├── rag_ui.py                  # Gradio web app
├── requirements.txt           # Python dependencies
└── README.md
```

---

##  Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/fin-rag.git
cd fin-rag

# 2. Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

##  How to Run

###  Option 1: CLI Mode

```bash
python app.py
```

###  Option 2: Gradio Web UI

```bash
python -m rag.rag_ui
```

>  Make sure `rag_ui.py` imports from the `rag/` folder properly, and all dependencies are installed.

---

##  Tech Stack

| Category            | Technology / Tool                                   | Purpose                                       |
|---------------------|-----------------------------------------------------|-----------------------------------------------|
| **Programming**     | Python                                              | Core language for the RAG pipeline            |
| **LLM Framework**   | LangChain (`langchain`, `langchain-community`)      | Retrieval-Augmented Generation flow           |
| **Embeddings**      | `sentence-transformers` (`all-MiniLM-L6-v2`)        | Text vectorization for semantic search        |
| **Vector Store**    | ChromaDB (`chromadb`)                               | Store & retrieve vectorized document chunks   |
| **PDF Parsing**     | PyMuPDF (`pymupdf`)                                 | Extract raw text from PDF                     |
| **Model Inference** | Hugging Face Transformers (`transformers`, `torch`) | Run text generation models (e.g. FLAN-T5)     |
| **Frontend**        | Gradio                                              | User interface for asking questions           |
| **Environment**     | Python Virtual Env                                  | Manage isolated dependencies                  |
| **Version Control** | Git + GitHub                                        | Code collaboration and versioning             |
