def mais_populoso(dicionario):
    dicionario2 = {}
    lista = []
    for estado in dicionario.keys():
        populacao_estado = 0
        dicionario2 = dicionario[estado]
        for municipio in dicionario2:
            populacao_municipio = dicionario2[municipio]
            populacao_estado += populacao_municipio
            dicionario2[estado] = populacao_estado
    for i in dicionario2.keys():
        lista.append(dicionario2[i])
    k = max(lista)
    dicionario[x] = k
    return x
        