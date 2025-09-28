from openai import OpenAI
import json

client = OpenAI(
    api_key="AIzaSyBu_z3AvcrGkMnnsyHhYOxIUrQtjZJPaEUsolve ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
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

print("\n\n\n\n")
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]
user_query = input(":-> ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",  # Use a valid model name
        messages=message_history
    )
    
    # Access the content correctly
    raw_result = response.choices[0].message.content  # Adjust based on the actual structure of `response`
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_results = json.loads(raw_result)

    if parsed_results.get("Step") == "START":
        print("STARTING\n", parsed_results.get("Description"))
        continue
    if parsed_results.get("Step") == "PLAN":
        print("THINKING\n", parsed_results.get("Description"))
        continue
    if parsed_results.get("Step") == "OUTPUT":
        print("THINKING\n", parsed_results.get("Description"))
        break