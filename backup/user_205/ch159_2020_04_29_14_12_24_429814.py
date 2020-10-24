import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

for i in dicionario:
    print (dicionario[quantidade])

    