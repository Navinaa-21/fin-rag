from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

def load_vectorstore(persist_directory="chroma_store"):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=persist_directory, embedding_function=embedding_model)

def generate_answer(vectorstore, query, model_name="google/flan-t5-base"):
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    input_text = f"Context:\n{context}\n\nQuestion: {query}"
    generator = pipeline("text2text-generation", model=model_name)
    result = generator(input_text, max_length=200, do_sample=False)
    return result[0]["generated_text"]
