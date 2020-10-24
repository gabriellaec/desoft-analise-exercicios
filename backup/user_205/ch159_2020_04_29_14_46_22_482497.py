import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)

lista = []
print(dicionario)
custo_total = 0
for lista in dicionario.values():
    for dicionario_na_lista in lista: 
        for chave,valor in dicionario_na_lista.items():
            dicionario_na_lista[chave]=lista.append(valor)
            
print (lista)

    