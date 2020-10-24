import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    dict = json.loads(conteudo)
    soma = 0
    for dictx in dict.values():
        for produto in dictx:
            soma += ((produto['quantidade']) * (produto['valor']))
        
    print(soma)