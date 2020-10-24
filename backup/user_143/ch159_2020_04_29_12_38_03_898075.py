import json
with open('estoque.json', 'r') as arquivo:
    texto=arquivo.read()
dicio=json.loads(texto)
v=0
for i in dicio['produtos']:
    v+=i['quantidade']*i['valor']
print(v)