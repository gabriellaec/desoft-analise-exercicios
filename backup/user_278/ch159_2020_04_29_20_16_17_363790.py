import json
with open("estoque.json","r") as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)
    
    total = 0
    
    for preço in estoque["produtos"]:
        total += preço["quatidade"] * preço["valor"]
    print (total)