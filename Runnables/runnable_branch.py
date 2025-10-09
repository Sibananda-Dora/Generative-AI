from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableBranch,RunnablePassthrough

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=""
)
parser=StrOutputParser

prompt1=PromptTemplate(
    template='Write a detailed report on the following topic.\n {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Summarize the following text.\n {text}',
    input_variables=['text']
)

generate_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x : len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)
final_chain=RunnableSequence(generate_chain,branch_chain)

print(final_chain.invoke({'topic':'elon vs trump'}))