def mais_populoso(dic):
    estado = dic.keys()
    print(estado)
    populacao = ''
    popest = {}
    i = 0
    #vai percorrer todos os valores
    for dv in dic.values():
        #v é o valor do valor do dic
        for v in dv:
            #pop total
            populacao += v
        popest[estado[i]] = populacao
        i+=1
    popanterior = 0
    for estado in popest.keys():
        if popest[estado]>popanterior:
            popanterior = pop[estado]
            estado_mais_pop = estado
    return estado_mais_pop,popanterior