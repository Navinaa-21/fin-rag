from langchain.text_splitter import CharacterTextSplitter

def split_text(text: str, chunk_size=1000, chunk_overlap=100):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.create_documents([text])
