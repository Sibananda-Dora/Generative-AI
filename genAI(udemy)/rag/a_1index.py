#indexing data using Pypdf tool from langchain

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path=Path(__file__).parent/"MySQLHandbook.pdf"

loader=PyPDFLoader(file_path=pdf_path)
docs=loader.load()
print(docs[1])