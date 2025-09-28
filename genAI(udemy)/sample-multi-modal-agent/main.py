from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBJleGk4PCwYg_kmKb1WTGMvRD7AA5VPzs",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type":"text","text":"Generate a caption fron the given image in about 20 words"},
                {"type":"image_url","image_url":{"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyIP0T92JSDFFMPlWoCBjRqEFh3AHZFMlSdg&s"}}
            ]
        }
    ]
)

print("Response:", response.choices[0].message.content)
