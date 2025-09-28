from openai import OpenAI
import json
client = OpenAI(
    api_key="AIzaSyAF1xlIR1fTdnYeN8T8oKvzmMn1Yhruc-g",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
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
d={"role": "system", "content": user_query}
message_history.append(d)
while True:
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type":"json_object"},
        messages=message_history
        
    )
    raw_result=response.choices[0].message.content
    message_history.append({"role":"assistant","content":raw_result})
    parsed_results=json.loads(raw_result)

    if parsed_results.get("Step")=="START":
        print("STARTING\n",parsed_results.get("Description"))
        continue
    if parsed_results.get("Step")=="PLAN":
        print("THINKING\n",parsed_results.get("Description"))
        continue
    if parsed_results.get("Step")=="OUTPUT":
        print("THINKING\n",parsed_results.get("Description"))
        break
print("\n\n\n\n")



# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={"type":"json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user","content": "give me a code which adds n numbers in js"}
#     ]
# )

# print(response.choices[0].message.content)

# import json
# json.dumps({"Step":})

# /*You should only and only answer the coding related questions.Do not answer anything else.If user asks anything other than coding based tell them that you can't answer and give them the justification yourself.But*/