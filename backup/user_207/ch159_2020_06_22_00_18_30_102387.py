import json

with open('estoque.json', 'r') as estoque_json:
    estoque = estoque_json.read()

# transforma para dicionario:
dicio_estoq = json.loads(estoque)

saldo = 0
for produto in dicio_estoq['produtos']:
    # cada produto é um elemento da lista (um dicionário)
    saldo += produto['quantidade']*produto['valor']

print (saldo)