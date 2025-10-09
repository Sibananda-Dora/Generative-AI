from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key="AIzaSyCVDThxo56lOp9fT9JfcrjWhU-1Opkg1kc"
)
parser=StrOutputParser()
prompt=PromptTemplate(
    template="Write a 500 word summary of the book Crime and Punishment by Dostoevsky.",
    input_variables=[]
)
chain=prompt|model|parser
result_text=chain.invoke({})

with open("summary.txt", "w") as f:
    f.write(result_text)

loader=TextLoader("summary.txt")
docs=loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)