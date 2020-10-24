import json

with open("estoque.json", "r", encoding="utf-8") as arquivo:
    estoque = arquivo.read()

soma = 0
dicionario = json.loads(estoque)
for produtos in dicionario.values():
    for produto in produtos:
        soma += (produto["quantidade"] * produto["valor"])
print(soma)