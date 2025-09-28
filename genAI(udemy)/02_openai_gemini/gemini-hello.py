from google import genai

client=genai.Client(
    api_key="AIzaSyAF1xlIR1fTdnYeN8T8oKvzmMn1Yhruc-g"
)

respose= client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What do you think about GUARDIANEYE "
)

print(respose.text)

