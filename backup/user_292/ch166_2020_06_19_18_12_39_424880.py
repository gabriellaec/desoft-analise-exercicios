def total_do_semestre_por_bairro(dic):
    dic_g ={}
    for i, n in dic.items():
        g = 0
        for x in range(len(n)):
            if  x >= 6:
                g += n[x]
            dic_g[i] = g
    return dic_g