from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("Rendezvous with Rama by Arthur C. Clarke 28juneday1.pdf")
docs=loader.load()
print(len(docs))
print(docs[5].page_content)
print(docs[5].metadata)