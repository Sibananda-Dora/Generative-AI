
#     user_query=input(">")
#     response= client.chat.completions.create(
#         model="gemini-2.5-flash",
#         messages=[
#             {"role":"user","content":user_query}
#         ]
#     )
#     print(f"{response.choices[0].message.content}")