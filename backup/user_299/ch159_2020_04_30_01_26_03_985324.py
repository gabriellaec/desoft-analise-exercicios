import json
with open ('estoque.json','r') as estoque:
    estoque = estoque.read()
   
dicionario = json.loads(estoque)

soma = 0
for e in dicionario.value():
    lista = e
    for f in lista:
        soma+=f['quantidade']*f['valor']
print(soma)
        