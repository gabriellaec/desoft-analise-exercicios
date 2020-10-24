def monta_mala(listapeso):
    m=0
    soma=0
    lista=[]
    while m<len(listapeso):
        soma+=listapeso[m]
        if soma <= 23:
            lista.append(listapeso[m])
            m+=1
        else:
            m+=1
            return lista