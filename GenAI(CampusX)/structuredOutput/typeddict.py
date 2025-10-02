from typing import TypedDict

class Demo(TypedDict):
    name: str
    age:int

Test:Demo={
    "name":"Sibanand",
    "age":"25"
}

print(Test)