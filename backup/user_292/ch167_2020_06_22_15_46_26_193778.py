def bairro_mais_custoso(dic):
    dic_g ={}
    for i, n in dic.items():
        g = 0
        for x in range(len(n)):
            if  x >= 6:
                g += n[x]
            dic_g[i] = g

    for i,n in dic_g.items():
        gasto = 0
        nome = ""
        if n > gasto:
            gasto = n 
            nome = i
    return nome
    
    return nome