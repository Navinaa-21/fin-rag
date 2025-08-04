from rag.pdf_reader import extract_text_from_pdf
from rag.text_chunker import split_text
from rag.embed_store import store_documents_in_chroma
from rag.retriever_generator import load_vectorstore, generate_answer
import os

PDF_PATH = r"C:\Users\Admin\Desktop\fin-rag\data\Personal-Finance-for-School-Students.pdf"

def build_or_load_rag():
    if not os.path.exists("chroma_store/index"):
        print("🔍 Reading and processing PDF...")
        text = extract_text_from_pdf(PDF_PATH)
        chunks = split_text(text)
        print(f"📄 Chunks created: {len(chunks)}")
        store_documents_in_chroma(chunks)
    else:
        print("✅ Vector store already exists.")
    return load_vectorstore()

if __name__ == "__main__":
    vectorstore = build_or_load_rag()

    print("\n🤖 Ask your personal finance questions!")
    while True:
        query = input("\n❓ Your question (or 'exit'): ")
        if query.lower() == "exit":
            break
        answer = generate_answer(vectorstore, query)
        print("\n💡 Answer:", answer)
