def mais_populoso(brasil):
    recorde = 0
    #estadomaispop = ''
    for estado, cidades in brasil.items():
        populacao = 0
        for pop in cidades.values():
            populacao += pop
        if populacao > recorde:
            recorde = populacao
            estadomaispop = estado
    return estadomaispop
        