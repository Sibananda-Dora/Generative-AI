from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


model=GoogleGenerativeAI(model="gemini-2.5-flash",api_key="")
parser= JsonOutputParser()
template1 = PromptTemplate(
    template='give me the name,age and city of a fictional person. How about Batman \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

chain= template1 | model | parser

result= chain.invoke({})
print(result)

