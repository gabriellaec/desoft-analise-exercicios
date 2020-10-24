import json
soma = 0

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    dict = json.loads(conteudo)
    for produto in dict:
        soma += (produto['quantidade'] * produto['valor'])
        
    print(soma)