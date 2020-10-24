def mais_populoso(dicionario):
    dic_pop_total = {}
    i = 0
    for dic in dicionario:
        #print(dic.values())
        pop = sum(dicionario[dic].values())
        dic_pop_total[dic] = pop

    maximo = max(dic_pop_total.values())
    for estado, pop in dic_pop_total.items():
        if maximo == pop:
            return estado