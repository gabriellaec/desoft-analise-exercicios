import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

lista = []
print(dicionario)
custo_total = 0
for lista in dicionario.values():
    for dic in lista: 
        for item in dic:
            dic[item]=lista.append(item)
            
print (lista)

    