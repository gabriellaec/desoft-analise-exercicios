import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    dict = json.loads(conteudo)
    lista = []
    for produto in dict.values():
        lista.append(produto['quantidade']) * (produto['valor'])
        
    print(sum(lista))