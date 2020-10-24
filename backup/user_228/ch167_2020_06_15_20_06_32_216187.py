def bairro_mais_custoso(empresa):
    for bairro in empresa:
        dic[gasto]=0
        for gasto in empresa[bairro][6:]:
            dic[gasto]+=gasto
    return dic
            
            
            