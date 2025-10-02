from langchain_google_genai import GoogleGenerativeAIEmbeddings

llm=GoogleGenerativeAIEmbeddings(
    model="gemini-2.5-flash",
    api_key=""
)
messages=[
    {"role":"system","content":"You are a helpful assistant that convert the user input to vector embeddinngs"},
    {"role":"user","content":"Hey,How are you ?"}
]
msg=llm.invoke(messages)
print(msg.content)