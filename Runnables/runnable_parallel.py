from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key="AIzaSyCVDThxo56lOp9fT9JfcrjWhU-1Opkg1kc"
)
model2=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="AIzaSyCVDThxo56lOp9fT9JfcrjWhU-1Opkg1kc"
)
prompt1=PromptTemplate(
    template='Generate a Tweet on the topic given below./n {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Generate a LinkedIN post on the topic given below./n {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
        "tweet":RunnableSequence(prompt1,model,parser),
        "linkedin":RunnableSequence(prompt2,model2,parser)
    }
)
print(parallel_chain.invoke({'topic':'Indo-Pak War'}))