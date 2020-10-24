def mais_populoso(pais):
    s = 0
    pop = ''
    for nome in pais.keys():
        for municipios, valor in pais[nome].items():
            y = pais[nome][municipios]
            d = sum(pais[nome].values())
        if d > s:
            s = d
            pop = nome
    return pop