from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=""
)
parser=StrOutputParser
prompt=PromptTemplate(
    template='Generate a random joke within two lines .',
    input_variables=[]
)
joke_chain=RunnableSequence(prompt,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'wordLength': RunnableLambda(lambda x: len(x.split()))
})
final_chain=RunnableSequence(joke_chain,parallel_chain)
print(final_chain.invoke({}))