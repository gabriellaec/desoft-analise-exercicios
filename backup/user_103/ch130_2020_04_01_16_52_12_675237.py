def monta_mala(listapeso):
    i=0
    soma=0
    lista1=[]
    while i<len(listapeso):
        soma+=listapeso[i]
        if soma <= 23:
            lista1.append(listapeso[i])
            i+=1
    return lista1
            