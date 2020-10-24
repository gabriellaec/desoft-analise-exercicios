import json
valor=0
with open('estoque.json','r') as arquivo:
    conteudo=json.load(arquivo)
    for i in conteudo['produtos']:
        valor += i['quantidade']*i['valor']
    print(valor)