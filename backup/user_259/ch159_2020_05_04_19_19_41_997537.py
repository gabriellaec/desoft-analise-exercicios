import json
with open('estoque.json', 'r') as estoque:
    itens = estoque.read()
valor = 0
dicionario = json.loads(itens)
lista = dicionario['produtos']
for i in lista:
    valor+=i['quantidade']*i['valor']
print(valor)