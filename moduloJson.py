import json 
dicc = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
cadena_json= json.dumps(dicc)
print(cadena_json)

cadena_json2 = '{"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}'
dicc2 = json.loads(cadena_json2)
print(dicc2)