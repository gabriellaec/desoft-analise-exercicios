def mais_populoso(dicionario):
    mais_populoso = 0
    for estados, cidades in dicionario.items():
        total = 0
        for populacao in cidades.values():
            total += populacao
        if total > mais_populoso:
            mais_populoso = total
            o_mais_populoso = estados
    return o_mais_populoso