import json
with open("estoque.json","r") as arquivo:
    return sum([prod["quantidade"]*prod["valor"] for prod in json.loads(arquivo.read())])