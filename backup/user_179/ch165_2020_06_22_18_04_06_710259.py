def mais_populoso(dicionario):
    totalPorEstado = []
    for i in range(len(dicionario)):
        diciEstado = dicionario.items()
        popMunicipios = diciEstado.values()
        poptotEstado = sum(popMunicipios)
        totalPorEstado.append(poptotEstado)
    maxPop = max(totalPorEstado)
    maispop = totalPorEstado.index(maxPop)
    return dicionario[maispop]