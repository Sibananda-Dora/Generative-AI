from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain.schema.runnable import RunnableParallel

model1=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="AIzaSyCVDThxo56lOp9fT9JfcrjWhU-1Opkg1kc"
)
model2=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key="AIzaSyCVDThxo56lOp9fT9JfcrjWhU-1Opkg1kc"
)
parser=StrOutputParser()
parser1=JsonOutputParser()
prompt1=PromptTemplate(
    template='give a generalised review on the following Book.\n {bookname}',
    input_variables=['bookname']
)
prompt2=PromptTemplate(
    template='give a quiz of 5 questions on the book.\n {bookname}',
    input_variables=['bookname'],
)
parallel_chain=RunnableParallel(
    {
        "review":prompt1|model1|parser,
        "quiz":prompt2|model2|parser
    }
)
prompt3=PromptTemplate(
    template='Merge and give a structured output of the review and quiz in the following format\n review ->{review}\n quiz ->{quiz}\n {format_instruction}',
    input_variables=['review','quiz'],
    partial_variables={'format_instruction':parser1.get_format_instructions()}
)
merge_chain=prompt3|model2|parser1
chain=parallel_chain|merge_chain
# result=chain.invoke({"bookname":"Animal Farm"})
# print(result)

chain.get_graph().print_ascii()