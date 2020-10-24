import json
with open('estoque.json') as estoque:
    estoque = estoque.read()
    dic_estoques = json.loads(estoque)
    montante =[]
    for produtos in dic_estoques.value():
        for produto in produtos:
            montante.append(produto['quantidade']*produto['valor']
    print(sum(montante))