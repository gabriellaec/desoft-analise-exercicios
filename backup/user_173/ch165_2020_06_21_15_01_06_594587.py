def mais_populoso(brasil):
    maior_populacao = 0
    maior_estado = ''
    for estado in brasil:
        populacao = 0
        for municipio,pop in pais[estado].items():
            populacao += pop
        if populacao > maior_populacao:
            maior_populacao = populacao
            maior estado = estado
        return maior_estado