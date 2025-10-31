import os
import pandas as pd 
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
# from langchain_community.vectorstores import FAISS
from sklearn.metrics.pairwise import cosine_similarity

# GEMINI_API_KEY = "AIzaSyAZGFt2dE7fxdQlgJQAi67eXM2Bt6qyBjQ" 

CSV_FILE_PATH = "my_data.csv"
# VECTOR_DB_DIR = "./"


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key="AIzaSyAZGFt2dE7fxdQlgJQAi67eXM2Bt6qyBjQ")
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",google_api_key="AIzaSyAZGFt2dE7fxdQlgJQAi67eXM2Bt6qyBjQ")

print("\n--- LangChain RAG System Initialized ---")
print(f"Using CSV file: {CSV_FILE_PATH}")

print("\n Loading and Splitting Data...")
try:
    loader = CSVLoader(file_path=CSV_FILE_PATH, encoding="utf-8")
    documents = loader.load()
    print(f"  Loaded {len(documents)} initial document(s) (one per row).")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    texts = text_splitter.split_documents(documents)
    print(f"  Split into {len(texts)} chunks for embedding.")

except Exception as e:
    print(f"  An error occurred during loading/splitting: {e}")
    exit()

print("\n Creating and Persisting Vector Store...")

vectorstore = Chroma(
    embedding_function=embeddings,
    collection_name="langchain",
    persist_directory="./chromadb",
)
vectorstore.add_documents(documents)

user_query = input("Enter your query: ")
loader2=TextLoader(user_query)
documents2=loader2.load()
embed2=embeddings.embed_query(user_query)

results = vectorstore.similarity_search(
    query=user_query,
    k=2
)
print("Similarity Search Results:", results)



# print("\n Setting up the Retrieval Chain...")

# retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type="stuff",
#     retriever=retriever,
#     return_source_documents=True
# )
# print("  RetrievalQA Chain established successfully.")


# print("\n--- Start Asking Questions ---")
# while True:
#     user_query = input("\nEnter your query (or type 'quit' to exit): \n> ")

#     if user_query.lower() == 'quit':
#         print("\nGoodbye! 👋")
#         break

#     if not user_query.strip():
#         continue

#     print("\n Searching and Generating Answer...")

#     try:
#         result = qa_chain.invoke({"query": user_query})

#         print("\n RAG Answer:")
#         print("--------------------------------------------------")
#         print(result['result'])
#         print("--------------------------------------------------")

#         print("\nSource Documents (Context Used for Answer):")
#         for i, doc in enumerate(result['source_documents']):
#             row_num = doc.metadata.get('row', 'N/A')
#             print(f"  - Source {i+1} (Row: {row_num}, File: {doc.metadata.get('source')}):")
#             print(f"    Content: {doc.page_content[:150]}...")

#     except Exception as e:
#         print(f"\n An error occurred during query processing: {e}")