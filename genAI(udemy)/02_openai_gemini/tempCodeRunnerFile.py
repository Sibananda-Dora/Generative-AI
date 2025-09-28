

# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={"type":"json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user","content": "give me a code which adds n numbers in js"}
#     ]
# )

# print(response.choices[0].message.content)