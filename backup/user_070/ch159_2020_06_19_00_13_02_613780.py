import json

with open('estoque.json', 'r') as arquivo_json:
    produtos = arquivo_json.read()
    
dicionario = json.loads(produtos)
prods = dicionario["produtos"]

valor = 0
for produto in prods:
    valor += (produto["quantidade"] * produto["valor"])

print(valor)