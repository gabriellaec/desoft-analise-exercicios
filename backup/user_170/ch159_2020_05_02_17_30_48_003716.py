import json
with open('estoque.json', 'r') as arquivo:
    estoque = arquivo.read()
dicionario  = json.loads(estoque)
produtos = dicionario['produtos']
valor = 0
for d in produtos:
    valor += float(d['quantidade'])*float(d['valor'])
print(valor)
        