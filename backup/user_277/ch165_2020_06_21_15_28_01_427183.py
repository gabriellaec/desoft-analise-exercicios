def mais_populoso(dicionario):
    dicionario2 = {}
    dicionario3 = {}
    for estado in dicionario.keys():
        populacao_estado = 0
        dicionario2 = dicionario[estado]
        for municipio in dicionario2:
            populacao_municipio = dicionario2[municipio]
            populacao_estado += populacao_municipio
            dicionario3[estado] = populacao_estado
    for e, p in dicionario3.items():
        variavel_e = e
        variavel_p = p
        if e >= variavel_e:
            variavel_p = p
    return variavel_p
        