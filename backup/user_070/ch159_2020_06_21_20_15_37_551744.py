import json

with open('estoque.json', 'r') as arquivo:
    estoque = arquivo.read()

estoque = json.loads(estoque)

valorfinal = 0

for produto in estoque["produtos"]:
    qntd = produto["quantidade"]
    valor = produto["valor"]
    valorfinal += (qntd * valor)
    
print(valorfinal)