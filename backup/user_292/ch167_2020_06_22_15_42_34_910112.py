def bairro_mais_custoso(dic):
    dic_g ={}
    for i, n in dic.items():
        g = 0
        for x in range(len(n)):
            if  x >= 6:
                g += n[x]
            dic_g[i] = g
    dic_gas = {}
    for n in dic_g.values():
        gasto = 0
        if n > gasto:
            gasto = n 
    dic_gas[i] = gasto
    return dic_gas