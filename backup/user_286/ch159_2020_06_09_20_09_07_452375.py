import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()

dicionario = json.loads(conteudo)

total = 0

for produto in dicionario['produtos']:
    total += produto['quantidade'] * produto['valor']

print(total)