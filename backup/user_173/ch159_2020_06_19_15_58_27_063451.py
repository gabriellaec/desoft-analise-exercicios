import json

with open('estoque.json','r') as estoque:
    estoque = estoque.read()
    dict_estoque = json.loads(estoque)
    montante = []
    for produtos in dict_estoque.values():
        montande.append(produto['quantidade']* produto['valor'])
    
    print(sum(montante))
                            