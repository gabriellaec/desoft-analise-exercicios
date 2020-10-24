import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

lista = []
print(dicionario)
custo_total = 0
for lista in dicionario.values():
    for dic in lista: 
        print (dic)
        for valores in dic.values():
            print (valores)
            lista.append(valores)
            
print (lista)

    