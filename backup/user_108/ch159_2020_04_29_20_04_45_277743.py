import json
with open("estoque.json","r") as arquivo:
    print([prod["quantidade"] for prod["valor"] in json.loads(arquivo.read())["produtos"]]])