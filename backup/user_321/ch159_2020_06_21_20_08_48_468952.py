import json 
with open ('estoque.json', 'r') as estoque:
    texto = estoque.read()
    
dicionario = json.loads(texto)

s = 0

for i in dicionario["produtos"]:
    s += i['quantidade']*i['valor']
print(s)