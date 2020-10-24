import json 
with open ('estoque.json', 'r') as estoque:
    texto = estoque.read()
    
dicionario = json.loads(texto)

s = 0

while i < len(dicionario):
    s += dicionario['quantidade']*dicionario['valor']
    i += 3
print(s)
    