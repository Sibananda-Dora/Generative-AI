import tiktoken
enc= tiktoken.encoding_for_model("gpt 4o")

text="Hey!! Myself Sibananda Dora"

dec= enc.encode(text)

print(dec)
