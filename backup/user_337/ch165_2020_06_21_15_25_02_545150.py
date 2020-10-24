def mais_populoso(dicionario_fofin):
    mais_populoso = 0
    for estado in dicionario_fofin:
        populacao = 0
        for cidade in dicionario_fofin[estado]:
            populacao += dicionario_fofin[estado][cidade]
        if populacao > mais_populoso:
            mais_populoso = populacao
            estado_populoso = estado
    return estado_populoso
