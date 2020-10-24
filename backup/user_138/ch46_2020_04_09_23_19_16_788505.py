def numero_no_indice(lista):
    i=0
    listaB=[]
    for a in lista:
        if a==i:
            listaB.append(a)
        i+=1
    return listaB