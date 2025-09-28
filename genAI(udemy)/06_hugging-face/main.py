from transformers import pipeline
import json


pipe = pipeline("text-generation", model="google/gemma-2-2b-it")


SYSTEM_PROMPT=''' 
 Let's  test something okay. So let's make this okay where user gives you a prompt and you try to solve using chain-of-thought where there is a start , plan(do some research on it and make more plans) and then provide the output

RULES:
-Strictly follow the output in json format

OUTPUT_FORMAT:{{"Step":"START | PLAN | OUTPUT" "Description":"string" or "numbers" but not null}} give one at a time

Examples:
START: 2*3-2 
PLAN: {{"Step":"PLAN" "Description":"for this calculation i will use the existing mathematics formulae"}} 
PLAN: {{"Step":"PLAN" "Description":"Let's try to solve this using BODMAS "}}
PLAN: {{"Step":"PLAN" "Description":"at first multiply 2 with 3  "}}
PLAN: {{"Step":"PLAN" "Description":"then subtract the result with 2   "}}
OUTPUT: {{"Step":"OUTPUT" "Description":" the solutin is 4"}}


'''

print("\n\\n\n\n")
message_history=[
     {"role": "system", "content": SYSTEM_PROMPT},
]
user_query=input(":->")
message_history.append({"role": "system", "content": user_query})
while True:
    # Prepare the input for the pipeline
    input_text = "\n".join([msg["content"] for msg in message_history])

    # Generate the response
    response = pipe(input_text, max_length=512, num_return_sequences=1)
    raw_result = response[0]["generated_text"]  # Extract the generated text

    # Append the assistant's response to the message history
    message_history.append({"role": "assistant", "content": raw_result})

    # Parse the result as JSON
    try:
        parsed_results = json.loads(raw_result)
    except json.JSONDecodeError:
        print("Error: The model did not return valid JSON.")
        break

    # Handle the parsed results
    if parsed_results.get("Step") == "START":
        print("STARTING\n", parsed_results.get("Description"))
        continue
    if parsed_results.get("Step") == "PLAN":
        print("THINKING\n", parsed_results.get("Description"))
        continue
    if parsed_results.get("Step") == "OUTPUT":
        print("THINKING\n", parsed_results.get("Description"))
        break

print("\n\n\n\n")