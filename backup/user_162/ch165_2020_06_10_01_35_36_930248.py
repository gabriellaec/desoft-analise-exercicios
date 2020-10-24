def mais_populoso(dic):
    pops = []
    estados = []
    for estado, cidade in dic.items():
        estados.append(estado)
        populacao = 0
        for pop in cidade.values():
            populacao+=pop
        pops.append(populacao)
     
    return estados[pops.index(max(pops))]