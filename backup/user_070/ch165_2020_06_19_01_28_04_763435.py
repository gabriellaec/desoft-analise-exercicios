def mais_populoso(brasil):
    recorde = 0
    for estado, cidades in brasil.items():
        tentativa = 0
        for pop in cidades.values():
            tentativa += pop
        if tentativa > recorde:
            maispop = estado
    return maispop