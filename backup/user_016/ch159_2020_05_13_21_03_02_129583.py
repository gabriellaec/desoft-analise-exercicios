import json
with open('estoque.json','r') as arquivo:
    conteudo = arquivo.read()
    dicionario1 = json.loads(conteudo)
    dicionario2 = dicionario1['produtos']
    dicionario3 = {}
    lista = []
    for i in range (len(dicionario2)):
        dicionario3 = dicionario2[i]
        lista.append(float(dicionario3['quantidade'])*float(dicionario3['valor']))
print(sum(lista))
    
    