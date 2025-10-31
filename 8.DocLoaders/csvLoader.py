from langchain_community.document_loaders import CSVLoader
from 


loader=CSVLoader("file.csv")
docs=loader.load()
print(docs[0].page_content)
print(len(docs))
for file in enumerate(docs):
    print(file)