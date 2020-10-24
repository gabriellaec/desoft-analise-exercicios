import json
with open(estoque.json, 'r') as arquivo:
    dicionario = json.loads(arquivo.read())
total = 0
for produto in dic['produtos']:
    total += produto['quantidade'] * produto['valor']
print(total)    
