import json

with open('estoque.json','r') as estoque:
    estoque = estoque.read()
    dict_estoque = json.loads(estoque)
    custo = []
    for produtos in dict_estoque.values():
        for produtos in produtos:
            custo.append(produto['quantidade']*produto['valor'])
    print(sum(custo)