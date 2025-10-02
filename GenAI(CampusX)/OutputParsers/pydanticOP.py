from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel ,Field

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=""
)

class Person(BaseModel):
    name:str=Field(description='Name of the person')
    age:int=Field(gt=18,description='Age of the person')
    city:str=Field(description='City of the person')

parser= PydanticOutputParser(pydantic_object=Person)

temp=PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain= temp|model|parser

final=chain.invoke({'place': 'russian'})
print(final)