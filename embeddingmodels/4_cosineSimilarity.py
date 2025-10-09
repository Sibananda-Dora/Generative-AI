from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=""
)
docs = [
    "After 12th you need to give an entrance exam to get into college.",
    "After college you need to find a job if necessary, otherwise you can also go towards higheer studies.",]
user_query = input(":=>")

embedDocs = embedding.embed_documents(docs)
embedQuery = embedding.embed_query(user_query)

print(cosine_similarity(embedDocs, [embedQuery]))
