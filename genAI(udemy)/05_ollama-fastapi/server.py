from fastapi import FastAPI,Body#fastapi dev filename.py
from ollama import Client

app=FastAPI()
client=Client(host="http://localhost:11434")


@app.get("/")
def read_root():
    return {"hello" : "world"}

@app.post("/chat")
def chat(
        message: str= Body(...,description="Message")
):
    response=client.chat(model="gemma2-2b", messages=[{
        "role": "user",
        "content": message
    }])

    return { "response": response.message.content}