import json

with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()
    
Estoque = json.loads(texto)
total = 0
for produto in Estoque['produtos']:
    quantidade = produto['quantidade']
    valor = produto['valor']
    total += (quantidade*valor)
    
print(total)