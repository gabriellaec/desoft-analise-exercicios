import json

custo = 0

with open("estoque.json", "r") as file:
    conteudo = file.read()
    produtos = json.loads(conteudo)["produtos"]
    for each in produtos:
        quantidade = float(each["quantidade"])
        valor = float(each["valor"])
        custo += quantidade*valor

print(custo)