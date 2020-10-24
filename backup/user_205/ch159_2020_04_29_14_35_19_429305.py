import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

print(dicionario)
custo_total = 0
for lista in dicionario.values():
    for subitem in lista: 
        print (subitem)

    