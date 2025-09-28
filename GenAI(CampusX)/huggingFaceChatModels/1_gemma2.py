# from transformers import AutoModelForCausalLM, AutoTokenizer
# from transformers import pipeline
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()

llm=HuggingFaceEndpoint(
        model_name="google/gemma-2-2b-it",
        api_key=os.getenv("hf_token"),
        task="text-generation",
)

llm=ChatHuggingFace(llm=llm)

result=llm.invoke("hello how are you?")
print(result.content)
