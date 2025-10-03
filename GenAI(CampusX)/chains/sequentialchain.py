from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="get your own"
)
parser=StrOutputParser()
parser1=JsonOutputParser()
prompt1=PromptTemplate(
    template='give a generalised review on the following Book.\n {bookname}',
    input_variables=['bookname']
)
prompt2=PromptTemplate(
    template='give a quiz of 5 questions on the review.\n {review}\n {format_instruction}',
    input_variables=['review'],
    partial_variables={'format_instruction':parser1.get_format_instructions()}
)
chain= prompt1|model|parser|prompt2|model|parser1
print(chain.invoke({"bookname":"Animal Farm"}))