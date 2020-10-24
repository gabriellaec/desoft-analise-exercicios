def encontra_maximo(l1):

    lista2 = []
    
    for i in l1:
        for t in i:
            lista2.append(abs(t))

    return(max(lista2))