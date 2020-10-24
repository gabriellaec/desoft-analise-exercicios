def mais_populoso(dicionario):
    dic_pop_total = {}
    i = 0
    for dic in dicionario:
        #print(dic.values())
        pop = sum(dicionario[dic].values())
        dic_pop_total[dic] = pop

    return max(dic_pop_total)