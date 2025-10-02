from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import StructuredOutputParser,ResponseSchema


model=GoogleGenerativeAI(model="gemini-2.5-flash",api_key="")

schema= [
    ResponseSchema(name='fact1',description='fact 1 about the topic'),
    ResponseSchema(name='fact2',description='fact 2 about the topic'),
    ResponseSchema(name='fact3',description='fact 3 about the topic'),
]
parser= StructuredOutputParser()

template=PromptTemplate(
    template='give 3 unique facts about our Universe.\n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instruutions':parser.get_format_instructions()},
)
chain= template | model| parser

final=chain.invoke({})
print(final)
