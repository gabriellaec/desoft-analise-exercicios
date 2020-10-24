def mais_populoso(dicionario):
    dicionario2 = {}
    dicionario3 = {}
    listae = []
    listap = []
    for estado in dicionario.keys():
        populacao_estado = 0
        dicionario2 = dicionario[estado]
        for municipio in dicionario2:
            populacao_municipio = dicionario2[municipio]
            populacao_estado += populacao_municipio
            dicionario3[estado] = populacao_estado
    for e, p in dicionario3.items():
        listae.append(e)
        listap.append(p)
        k = max(listap)
        r = listap.find(k)
        final = listae[k]
    return final
        