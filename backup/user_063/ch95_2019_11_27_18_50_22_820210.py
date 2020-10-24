def mais_populoso(brasil):
    estado = []
    populacao = []
    for key in brasil:
        est = key
        estado.append(est)
        city = brasil[key]
        for key in city:
            pop = city[key]
            populacao.append(pop)
    return (estado, populacao)