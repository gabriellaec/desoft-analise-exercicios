import json
with open('estoque.json', 'r') as arquivo:
    #texto = arquivo.read()
    estoque = json.load(arquivo)
    valor = 0
    for produto in estoque['produtos']:
        valor += produto['quantidade']*produto['valor']
    print(valor)