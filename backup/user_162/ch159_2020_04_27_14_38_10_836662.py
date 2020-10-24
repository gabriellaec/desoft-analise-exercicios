import json


with open('estoque.json', 'r') as arquivo:
    texto = arquivo.read()
    quantidade = json.loads(texto)
    valor = 0
    
    
for i in quantidade["produtos"]:
    valor += i["quantidade"] * i["valor"]
print(valor)

