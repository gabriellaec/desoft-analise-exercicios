def encontra_maximo (matriz):
    lista0 = matriz[0]
    lista1 = matriz[1] 
    lista2 = matriz[2]
    maximo = lista0[0]
    for e in lista0:
        if e > maximo:
            maximo = e
        for e1 in lista1:
            if e1 > maximo:
                maximo = e1
            for e2 in lista2:
                if e2 > maximo:
                    maximo = e2
    return maximo