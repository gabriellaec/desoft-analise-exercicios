import json
with open("estoque.json","r") as arquivo:
    print([prod for prod in json.loads(arquivo.read())])