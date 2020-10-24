import json

with open('estoque.json') as arquivo:
    
    dados = json.load(arquivo)
    print(dados)