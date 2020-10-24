import json
with open('estoque.json', 'r') as arquivo:
    texto = arquivo.read()
dicio = json.loads(texto)
preco =0
for n in dicio["produtos"]:
    preco += n["quantidade"]*n["valor"]
print(preco)
    