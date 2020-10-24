import json

with open('estoque.json') as arquivo:
    produtos = json.load(arquivo)['produtos']
    
valor = 0
    
for produto in produtos:
    valor += float(produto['quantidade']) * float(produto['valor'])
    
print(valor)