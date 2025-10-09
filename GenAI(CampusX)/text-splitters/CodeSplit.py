from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
import os

current_dir = os.path.dirname(__file__)
path = os.path.join(current_dir, "length_based.py")

with open(path, 'r', encoding='utf-8') as file:
    code_content = file.read()

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=150,
    chunk_overlap=0
)

chunks=splitter.split_text(code_content)
print(len(chunks))
for chunk in enumerate(chunks):
    print(chunk)
