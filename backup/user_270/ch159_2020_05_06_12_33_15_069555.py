import json
with open("estoque.json", "r") as arquivo:
    cont = arquivo.read()
dic = json.loads(cont)
soma = 0
for i in dic["produtos"]:
    valor_ = i['quantidade']*i["valor"]
    soma += valor
print(soma)
    