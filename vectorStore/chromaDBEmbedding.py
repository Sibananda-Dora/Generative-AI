#NOT YET COMPLETED
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

model=GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key="AIzaSyBSBl2K8DI1RGG5LKK1dF2tOo3sD9GCVEc"
)

doc1=Document(
    page_content="Hello, how are you ?",
    metadata={"category":"conversation"}
)

doc2=Document(
    page_content="Python is a high-level programming language known for its simplicity and readability.",
    metadata={"category":"programming"}
)

doc3=Document(
    page_content="Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
    metadata={"category":"AI"}
)

doc4=Document(
    page_content="Vector databases are specialized systems designed to store and retrieve high-dimensional vectors efficiently.",
    metadata={"category":"database"}
)
docs=[doc1,doc2,doc3,doc4]

vector_store=Chroma(
    embedding_function=model,
    collection_name="langchain",
    persist_directory="./chromadb"
)

vector_store.add_documents(docs)
# vector_store.get(include=['emebddings','documents','metadata'])

vector_store.similarity_search(
    query="",
    k=2
)
vector_store.similarity_search_with_score(
    query="",
    fikter={"category":"AI"}
)
doc3_updated=Document(
    page_content="Machine learning is a subset of AI that enables systems to learn from data.",
    metadata={"category":"AI"}
)
vector_store.update_documents(document_id="",document=do'cs)
vector_store.delete(ids='','')'
# vector_store.get(include=['emebddings','documents','metadata'])
