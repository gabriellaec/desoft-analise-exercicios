def mais_populoso(dicionario):
    populacao_estado = 0
    lista = []
    for estado in dicionario.keys():
        dicionario2 = dicionario[estado]
        for municipio in dicionario2:
            populacao_municipio = dicionario2[municipio]
            populacao_estado += populacao_municipio
        lista.append(populacao_estado)
    a = max(lista)
    return a
        