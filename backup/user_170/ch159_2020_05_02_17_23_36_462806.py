import json
with open('estoque.json', 'r') as arquivo:
    estoque = arquivo.read()
dicionario  = json.loads(estoque)
print(dicionario)