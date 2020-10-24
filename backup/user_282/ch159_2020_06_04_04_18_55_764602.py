import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)
    count = 0
    for i in estoque['produtos']:
        count += i["quantidade"] * i["valor"]

print(count)