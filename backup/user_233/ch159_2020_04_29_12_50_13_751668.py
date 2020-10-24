import json

with open('estoque.json') as arquivo:
    
    estoque = json.load(arquivo)
    
    for x in estoque: print(x)