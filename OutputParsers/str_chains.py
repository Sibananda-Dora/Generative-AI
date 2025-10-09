from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model=GoogleGenerativeAI(model="gemini-2.5-flash",api_key="")

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)
parser=StrOutputParser()

chain= template1 | model | parser | template2 | model |parser

result= chain.invoke({'topic':'black hole'})

print(result)

