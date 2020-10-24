import json

with open('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)
    total_produtos = 0
    for i in estoque["produto"]:
        total += i["quantidade"] * i["valor"]
    print(total)
                                     