def encontra_maximo(lista):
    lista1=lista[0]
    lista2=lista[1]
    lista3=lista[2]
    i=0
    termo_anterior=lista1[0]
    while len(lista1)>i:
        if lista1[i]<0:
            lista1[i]=lista1[i]*-1
        if termo_anterior<lista1[i]:
            termo_anterior=lista1[i]
            i+=1
        else:
            i+=1
    i=0
    while len(lista2)>i:
        if lista2[i]<0:
            lista2[i]=lista2[i]*-1
        if termo_anterior<lista2[i]:
            termo_anterior=lista2[i]
            i+=1
        else:
            i+=1
    i=0
    while len(lista3)>i:
        if lista3[i]<0:
            lista3[i]=lista3[i]*-1
        if termo_anterior<lista3[i]:
            termo_anterior=lista3[i]
            i+=1
        else:
            i+=1
    return termo_anterior