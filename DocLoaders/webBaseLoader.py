#logic is wrong. you can load your own webLinks and modify the code.
from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
loader=WebBaseLoader(
    [
        "https://en.wikipedia.org/wiki/Christopher_Nolan",
        "https://en.wikipedia.org/wiki/Martin_Scorsese"
    ]
)
loader.requests_per_second=1
docs=loader.load()
print(len(docs))
for doc in enumerate(docs):
    print(doc[1])

