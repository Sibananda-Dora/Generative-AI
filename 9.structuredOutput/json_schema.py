from jsonschema import validate,ValidationError

schema={
    "title":"student",
    "description":"schema introduction",
    "type":"object",
    "properties":{
        "name":{"type":"string"},
        "age":{"type":"integer"}

    },
    "required": ["name"]
}

response={"name":"Sibananda","age":25}

try:
    validate(instance=response,schema=schema)
    print("Validation Successful")
except ValidationError as e :
    print(e.message)

