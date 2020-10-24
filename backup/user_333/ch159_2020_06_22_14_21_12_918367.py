import json

with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()
    
Estoque = json.loads(texto)
valor = 0
for i in range(len(Estoque)):
    produto = Estoque[i]
    quantidade = produto['quantidade']
    valor = produto['valor']
    valor += quantidade*valor
    
print(valor)