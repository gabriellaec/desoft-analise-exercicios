import json

with open ('estoque.json', 'r') as arquivo:
    estoque = arquivo.read()
    
estoque = json.loads(estoque)
valor_final = 0

for produto in estoque["produtos"]:
    quant = produto["quantidade"]
    valor = produto["valor"]
    
    valor_final += (quant*valor)
    
print(valor_final)
    
    