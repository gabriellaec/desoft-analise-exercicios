def mais_populoso(dicionario):
    mais_populoso = 0
    for estados in dicionario.values():
        total = 0
        for municipio, populacao in estados.items():
            total += populacao
        if total > mais_populoso:
            mais_populoso = total
    o_mais_populoso = estados
    return o_mais_populoso