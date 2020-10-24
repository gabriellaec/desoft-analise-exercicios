def mais_populoso(dic):
    dic_pop = dict()
    for e in dic:
        maior_pop = 0
        for i in dic[e]:
            cidades = dic[e]
            dic_pop[e] = cidades[i]
            if maior_pop < dic_pop[e]:
                maior_pop = dic_pop[e]
    return maior_pop