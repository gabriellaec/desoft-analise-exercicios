import json
valor=0
with open('estoque.json','r') as arquivo:
    conteudo=arquivo.read()
    for i in range(len(conteudo['produtos'])):
        valor += produtos[i]['quantidade']*['valor']
    print(valor)