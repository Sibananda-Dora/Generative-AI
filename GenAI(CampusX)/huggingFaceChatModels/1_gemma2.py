# from transformers import AutoModelForCausalLM, AutoTokenizer
# from transformers import pipeline
from openai import OpenAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import json
load_dotenv()

llm=HuggingFaceEndpoint(
        model="google/gemma-2-2b-it",
        huggingfacehub_api_token=os.getenv("hf_token"),
        task="text-generation",
)
SYSTEM_PROMPT = ''' 
You should follow the steps mentioned where user gives you a prompt and you try to solve using chain-of-thought where there is a start, plan (do some research on it and make more plans), and then provide the output.'only coding based answers and if the users tells to  solve anything beside coding then say sorry

RULES:
- Strictly follow the output in JSON format.

OUTPUT_FORMAT: {{"Step":"START | PLAN | OUTPUT", "Description":"string" or "numbers" but not null}} give one at a time.

Examples:
START: 2*3-2 
PLAN: {{"Step":"PLAN", "Description":"for this calculation I will use the existing mathematics formulae"}} 
PLAN: {{"Step":"PLAN", "Description":"Let's try to solve this using BODMAS"}}
PLAN: {{"Step":"PLAN", "Description":"at first multiply 2 with 3"}}
PLAN: {{"Step":"PLAN", "Description":"then subtract the result with 2"}}
OUTPUT: {{"Step":"OUTPUT", "Description":"the solution is 4"}}
'''

client=ChatHuggingFace(llm=llm)

# result=client.invoke("hello how are you?")
# print(result.content)


print("\n\n\n\n")
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]
user_query = input(":-> ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.invoke(user_query)
    
    # Access the content correctly
    raw_result = response.content 
    print(raw_result) # Adjust based on the actual structure of `response`
#     message_history.append({"role": "assistant", "content": raw_result})
#     parsed_results = json.loads(raw_result)

#     if parsed_results.get("Step") == "START":
#         print("STARTING\n", parsed_results.get("Description"))
#         continue
#     if parsed_results.get("Step") == "PLAN":
#         print("THINKING\n", parsed_results.get("Description"))
#         continue
#     if parsed_results.get("Step") == "OUTPUT":
#         print("THINKING\n", parsed_results.get("Description"))
#         break
