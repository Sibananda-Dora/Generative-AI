from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path="./directory",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
docs=loader.load()
print(docs[10].page_content)
