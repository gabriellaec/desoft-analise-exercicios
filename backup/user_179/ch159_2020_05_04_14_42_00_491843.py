import json

with open('estoque.json', 'r') as texto:
    estoques = texto.read()
    
dicionario = json.loads(estoques)
valores = dicionario.values()

total = 0
i = 1
while i < len(valores)/3:
    total = total + valores[1+3*i] * valores[2+3*i]
    i = i + 1
    
print(total)