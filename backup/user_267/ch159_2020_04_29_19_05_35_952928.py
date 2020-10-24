import json
with open('estoque.json', 'r') as arquivo:
    texto = arquivo.read()
dicio = json.loads(texto)
preco =0
for n in dicio:
    preco += dicio['quantidade']*dicio['valor']
print(preco)
    