def mais_populoso(dicionario):
    dicionario2 = {}
    dicionario3 = {}
    variavel_p = 0
    for estado in dicionario.keys():
        populacao_estado = 0
        dicionario2 = dicionario[estado]
        for municipio in dicionario2:
            populacao_municipio = dicionario2[municipio]
            populacao_estado += populacao_municipio
            dicionario3[estado] = populacao_estado
    for e, p in dicionario3.items():
        if p >= variavel_p:
            variavel_p = p
            variavel_e = e
    return variavel_e
        