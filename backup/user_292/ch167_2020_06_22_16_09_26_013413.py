    dic_g ={}
    for i, n in dic.items():
        g = 0
        for x in range(len(n)):
            if  x >= 6:
                g += n[x]
            dic_g[i] = g
    gasto = 0
    for y in dic_g.values():
        if y > gasto:
            gasto = y
    nome = ""
    for z in dic_g.keys():
        if dic_g[z] == gasto:
            nome = z
    return nome