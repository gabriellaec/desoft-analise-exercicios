import json 
with open ('estoque.json', 'r') as estoque:
    texto = estoque.read()
    
dicionario = json.loads(texto)

for i in dicionario:
    if i == 'quantidade':
        e = dicionario[i]
    elif i == 'valor':
        s += e*dicionario[i]
    