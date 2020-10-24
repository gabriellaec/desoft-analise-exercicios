import json
with open("estoque.json","r") as arquivo:
    print([prod["quantidade"] * prod["valor"] for prod in json.loads(arquivo.read())["produtos"]])