def verifica_preco(x,y,z):
    dic1 = {}
    dic2 = {}
    for x, cor in y.items():
        dic1[x] = cor
        for dic1[x], valor in z.items():
            dic2[dic1[x]] = valor
    return valor


        
    