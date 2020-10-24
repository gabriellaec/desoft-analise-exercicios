import json

custo = 0

with open("estoque.json", "r") as file:
    conteudo = file.read()
    produtos = json.loads(conteudo)["produtos"]
    for prod in produtos:
        quantidade = int(prod["quantidade"])
        valor = float(prod["valor"])
        custo += quantidade*valor

print(custo)