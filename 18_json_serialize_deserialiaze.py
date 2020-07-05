# 18. Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json

dict1 = {'name': 'Dev', 'age': 26}      # dict1 is a python object
print("Originally: ",dict1)
print(type(dict1))
json_string = json.dumps(dict1)         # serialization: converting object into byte stream
print("After serialization: ", json_string)
print(type(json_string))
data = json.loads(json_string)          # Deserialization: converting byte stream into object
print("After deserialization: ",data)
print(type(data))
