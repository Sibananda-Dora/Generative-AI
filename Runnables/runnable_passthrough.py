from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=""
)

prompt=PromptTemplate(
    template='Generate a random joke within two lines .',
    input_variables=[]
)

parser=StrOutputParser()

# joke_chain=prompt | model | parser

joke_chain=RunnableSequence(prompt,model,parser)
prompt2=PromptTemplate(
template='Write the explaination to the following joke : {topic}',
input_variables=['topic']
)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_chain,parallel_chain)
print(final_chain.invoke({}))


# explaination_chain=prompt2 | model | parser

