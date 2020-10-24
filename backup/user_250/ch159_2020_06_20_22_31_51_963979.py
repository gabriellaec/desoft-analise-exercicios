import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    dict = json.loads(conteudo)
    soma = 0
    for produto in dict:
        soma + = (produto['quantidade']) * (produto['valor'])
        
    print(soma)