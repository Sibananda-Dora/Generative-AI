from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding=GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key="",
    dimensions="300"
)
user_query=input(":->")
response=embedding.embed_query(user_query)
response[:5]
print(response[:5])