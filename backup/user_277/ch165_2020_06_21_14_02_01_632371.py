def mais_populoso(dicionario):
    dicionario2 = {}
    lista = []
    dicionario3 = {}
    for estado in dicionario.keys():
        populacao_estado = 0
        dicionario2 = dicionario[estado]
        for municipio in dicionario2:
            populacao_municipio = dicionario2[municipio]
            populacao_estado += populacao_municipio
            dicionario3[estado] = populacao_estado
    for i in dicionario3.keys():
        lista.append(dicionario3[i])
    k = max(lista)
    return k
        