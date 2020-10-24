import json

with open('estoque.json', 'r') as arquivo:
    texto = arquivo.read()

dicionario=json.loads(texto)
estoque=dicionario['produtos']

valor=0
for i in range (0,len(estoque)):
    qtd=estoque [i]['quantidade']
    preco=estoque [i]['valor']
    mult=preco*qtd
    valor+=mult
print (valor)