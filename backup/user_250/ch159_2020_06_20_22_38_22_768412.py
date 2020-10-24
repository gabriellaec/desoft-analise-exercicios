import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    dict = json.loads(conteudo)
    lista = []
    for dictx in dict.values():
        for produto in dictx:
            lista.append((produto['quantidade']) * (produto['valor']))
        
    print(sum(lista))