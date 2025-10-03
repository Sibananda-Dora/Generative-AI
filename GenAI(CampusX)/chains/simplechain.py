from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=""
)
parser=StrOutputParser()
prompt1=PromptTemplate(
    template='give a generalised review on the following Book.\n {bookname}',
    input_variables=['bookname']
)

chain= prompt1|model|parser
print(chain.invoke({"bookname":"Animal Farm"}))