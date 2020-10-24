import json

with open ('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()

conteudo = json.loads(conteudo)
total = 0
for produto in conteudo['produtos']:
    qnt = produto['quantidade']
    vlr = produto['valor']
    total += qnt*vlr
print(total)