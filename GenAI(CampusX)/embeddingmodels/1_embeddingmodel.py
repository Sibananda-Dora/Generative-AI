from langchain_huggingface import HuggingFaceEmbeddings

# small + fast
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2")

text = "Delhi is the capital of India."
vector = embedding.embed_query(text)

print(f"Embedding length: {len(vector)}")
print(vector[:10])  # show first 10 dims
