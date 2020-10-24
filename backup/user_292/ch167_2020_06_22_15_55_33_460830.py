def bairro_mais_custoso(dic):
    dic_g ={}
    for i, n in dic.items():
        g = 0
        for x in range(len(n)):
            if  x >= 6:
                g += n[x]
            dic_g[i] = g

    for n in dic_g.values():
        gasto = 0
        if n > gasto:
            gasto = n 
    for i in dic_g.keys():
        if dic_g[i] == gasto:
            return i 