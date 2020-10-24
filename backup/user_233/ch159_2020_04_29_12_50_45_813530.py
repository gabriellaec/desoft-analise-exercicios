import json

with open('estoque.json') as arquivo:
    
    produtos = json.load(arquivo)['produtos']
    
    for x in produtos: print(x)