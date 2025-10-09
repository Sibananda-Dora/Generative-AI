# from openai import OpenAI
# import requests
# client = OpenAI(
#     api_key="AIzaSyBu_z3AvcrGkMnnsyHhYOxIUrQtjZJPaEU",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
# # )
# SYSTEM_PROMPT=''' 
#  Let's  test something okay. So let's make this okay where user gives you a prompt and you try to solve using chain-of-thought where there is a start , plan(do some research on it and make more plans) and then provide the output.You can also use the tools from the list of available tools.

# RULES:
# -Strictly follow the output in json format
# -only runs once at a time
# -Sequence of steps is start ,plan,observe  if needed and finally give the output
# -for every tool call wait for the observe step which is the output from the step called to

# OUTPUT_FORMAT:{{"Step":"START" | "PLAN" | "OUTPUT" "Description":"string" or "numbers" |"TOOL":"string","input":"string"}}

# Available Tools:
# -get_weather(city:str):takes city name as an input and returns the weather info about the current weather in the city

# Examples:
# 1.
# START: 2*3-2 
# PLAN: {{"Step":"PLAN" "Description":"for this calculation i will use the existing mathematics formulae"}} 
# PLAN: {{"Step":"PLAN" "Description":"Let's try to solve this using BODMAS "}}
# PLAN: {{"Step":"PLAN" "Description":"at first multiply 2 with 3  "}}
# PLAN: {{"Step":"PLAN" "Description":"then subtract the result with 2   "}}
# OUTPUT: {{"Step":"OUTPUT" "Description":" the solutin is 4"}}

# 2.
# START: fetch me the weather of mumbai .
# PLAN: {{"Step":"PLAN" "Description":"Seems like the user is interested in knowing the weather of mumbai"}} 
# PLAN: {{"Step":"PLAN" "Description":"Let's see if we have any available tools to get the weather "}}
# PLAN: {{"Step":"PLAN" "Description":"great we have get_weather tool availlable for this query"}}
# PLAN: {{"Step":"PLAN" "TOOL": "get_weather" "input":"mumbai"}}
# OUTPUT: {{"Step":"OBSERVE" "Description":"The temperature of delhi is 20 degree C "}}
# PLAN: {{"Step":"PLAN" "Description":"great we got the weather of delhi,let's return it to the user"}}
# OUTPUT: {{"Step":"OUTPUT" "Description":" The current weather in Mumbai is 20 degree Celsius with some cloudy sky."}}



# '''
# def get_weather(city: str):
#     url=f"https://wttr.in/{city}?format=%C+%t"
#     response=requests.get(url)
#     if response.status_code==200:
#         return f"The weather in {city} is {response.text}"
    
#     return "Something went wrong"



# def main():
#     message_history = [
#     {"role": "system", "content": SYSTEM_PROMPT},
# ]
#     user_query=input(">")
#     if "STEP"=="TOOL":
#         choices[0].message.content.get("tool")
#     message_history.append({"role": "user", "content": user_query})
#     response= client.chat.completions.create(
#         model="gemini-2.5-flash",
#         messages=[
#             {"role":"user","content":user_query}
#         ]
#     )
#     print(f"{response.choices[0].message.content}")

# # main()
# main()

from openai import OpenAI
import requests
import json

# Initialize the OpenAI client
client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# System prompt
SYSTEM_PROMPT = ''' 
Let's test something okay. So let's make this okay where user gives you a prompt and you try to solve using chain-of-thought where there is a start, plan (do some research on it and make more plans), and then provide the output. You can also use the tools from the list of available tools.

RULES:
- Strictly follow the output in JSON format
- Only runs once at a time
- Sequence of steps is start, plan, observe if needed, and finally give the output
- For every tool call, wait for the observe step which is the output from the step called to

OUTPUT_FORMAT: {{"Step":"START" | "PLAN" | "OUTPUT", "Description":"string" or "numbers", "TOOL":"string", "input":"string"}}

Available Tools:
- get_weather(city:str): takes city name as an input and returns the weather info about the current weather in the city
'''

# Function to get weather information
def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong"

# Main function to handle user queries
def main():
    message_history = [
        {"role": "system", "content": SYSTEM_PROMPT},
    ]
    user_query = input("> ")
    message_history.append({"role": "user", "content": user_query})

    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gemini-2.5-flash",  # Ensure this is a valid model name
        messages=message_history
    )

    # Parse the response
    try:
        raw_result = response.choices[0].message.content
        print(f"Raw Response: {raw_result}")
        parsed_result = json.loads(raw_result)

        # Handle TOOL step
        if parsed_result.get("Step") =="TOOL" in parsed_result:
            tool_name = parsed_result["TOOL"]
            tool_input = parsed_result["input"]
            if tool_name == "get_weather":
                tool_output = get_weather(tool_input)
                print(f"Tool Output: {json.dumps(tool_output,indent=4)}")
                return

        # Handle OUTPUT step
        if parsed_result.get("Step") == "OUTPUT":
            print(f"Output: {parsed_result.get('Description')}")

    except json.JSONDecodeError:
        print("Error: The model did not return valid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
main()