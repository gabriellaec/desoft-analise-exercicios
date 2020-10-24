import json
with open('estoque.json', 'r') as arquivo:
    texto = arquivo.read()
dicio = json.loads(texto)
for n in dicio:
    preco += dicio['quantidade']*dicio['valor']
print(preco)
    