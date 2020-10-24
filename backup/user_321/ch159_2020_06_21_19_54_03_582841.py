import json 
with open ('estoque.json', 'r') as estoque:
    texto = estoque.read()
    
dicionario = json.loads(texto)

s = 0

for i in dicionario:
    if i == 'quantidade':
        print (i,dicionario[i])
        e = dicionario[i]
    elif i == 'valor':
        print (i,dicionario[i])
        s += e*dicionario[i]
print(s)
    