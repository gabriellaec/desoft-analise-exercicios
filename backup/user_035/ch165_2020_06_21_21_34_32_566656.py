def mais_populoso(pais):
    maior_populacao = 0
    maior_estado = ''
    for estado in pais:
        populacao = 0
        for municipio, pop in pais[estado].itens():
            populacao += pop
        if populacao > maior_populacao:
            maior_populacao = populacao
            maior_estado = estado
    return maior_estado