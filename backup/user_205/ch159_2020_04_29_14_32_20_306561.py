import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

print(dicionario)

for i in dicionario.values():
    separa = i.split(',')
    print (separa)

    