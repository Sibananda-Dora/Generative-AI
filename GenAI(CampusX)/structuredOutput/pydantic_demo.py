from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class Demo(BaseModel):
    name: str
    age:Optional[int]= None
    email:EmailStr
    cgpa:float =Field(gt=0,lt=10,default=5,description="A decimal value representing the cgpa of the student")
Test={
    "name":"Sibananda",
    "age": 25,
    "email":"abecd@gmil.com"

}
obj=Demo(**Test)
obj_dict=dict(obj)
print(obj_dict)