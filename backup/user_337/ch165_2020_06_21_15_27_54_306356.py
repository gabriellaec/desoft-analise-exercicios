def mais_populoso(brasil):
    mais_populoso = 0
    populacao = 0
    for estado in brasil:
        for cidade in brasil[estado]:
            populacao += brasil[estado][cidade]
        if populacao > mais_populoso:
            mais_populoso = populacao
            estado_populoso = estado
    return estado_populoso
