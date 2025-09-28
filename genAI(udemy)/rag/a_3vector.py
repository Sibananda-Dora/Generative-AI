#split/chunking data using Pypdf tool from langchain

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore


pdf_path=Path(__file__).parent/"MySQLHandbook.pdf"
#index
loader=PyPDFLoader(file_path=pdf_path)
docs=loader.load()

#splitter
text_splitter= RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks=text_splitter.split_documents(documents=docs)

embedding_model=OllamaEmbeddings(
    model="gemma2-2b"
)

vector_store=QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:3000",
    collection_name="learning rag"
)

