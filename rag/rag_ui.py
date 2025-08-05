import gradio as gr
from rag.retriever_generator import load_vectorstore, generate_answer

# Load the vectorstore only once when the app starts
vectorstore = load_vectorstore()

# Function to run the RAG pipeline for a query
def answer_question(query):
    if not query.strip():
        return "Please enter a question."
    try:
        answer = generate_answer(vectorstore, query)
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
iface = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(lines=2, placeholder="Ask a question about personal finance..."),
    outputs="text",
    title="📚 Personal Finance Chatbot",
    description="Ask any question based on the 'Personal Finance for Students' PDF.",
    theme="soft"
)

# Launch the app
if __name__ == "__main__":
    iface.launch(
    server_name="0.0.0.0",  # or try "localhost"
    server_port=5050,       # change from default 7860
    share=False,            # avoid tunneling via Gradio
    inbrowser=True          # auto-open browser
)


