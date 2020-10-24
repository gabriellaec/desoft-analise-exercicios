def mais_populoso(dic):
    maiorpop = 0
    for mun,cid in dic.items():
        populacao =0
        for pop in cid.values():
            populacao += pop
        if populacao > maiorpop:
            maiorpop = populacao
    return mun