import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

print(dicionario)
custo_total = 0
for lista in dicionario.values():
    for dicionario_na_lista in lista: 
        for item in dicionario_na_lista:
            custo += dicionario_na_lista[item]*
        print (subitem)

    