import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

print(dicionario)

for lista in dicionario.values():
    for subitem in lista: 
        separa = subitem.split(',')
        print (separa)

    