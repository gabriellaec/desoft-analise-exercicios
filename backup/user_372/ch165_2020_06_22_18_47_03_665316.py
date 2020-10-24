def mais_populoso(dicionario):
    maior_populacao = 0
    for estado in brasil:
        populacao = 0
        for cidade in brasil[estado]:
            populacao += brasil[estado][cidade]
        if populacao > maior_populacao:
            maior_populacao = populacao
            nome_estado = estado
    return nome_estado
