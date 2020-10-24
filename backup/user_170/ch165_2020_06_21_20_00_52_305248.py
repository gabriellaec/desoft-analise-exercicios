def mais_populoso(dic):
    popTotal = {}
    for i,a in dic.items():
        soma = 0
        for v in a.values():
            soma += v
        popTotal[i] = soma
    return max(popTotal, key = popTotal.get)