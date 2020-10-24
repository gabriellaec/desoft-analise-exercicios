import json
soma = 0

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    dict = json.loads(conteudo)
    for produto in dict:
        soma += (float(produto['quantidade']) * float(produto['valor']))
        
    print(soma)