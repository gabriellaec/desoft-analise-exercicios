def estritamente_crescente(lista1):
    i=0
    lista2=[]
    lista2.append(lista[i])
    v=True
    while i<(len(lista1)-1) and v==True:
        if lista1[i]<lista1[i+1]:
            lista2.append(lista1[i+1])
        else:
            v=False
        i=i+1
    return lista2