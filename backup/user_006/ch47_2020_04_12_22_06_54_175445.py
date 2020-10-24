def estritamente_crescente(lista1):
    lista2=[lista1[0]]
    v=True
    i=0
    while i<(len(lista1)-1) and v==True:
        if lista1[i]<lista1[i+1]:
            lista2.append(lista1[i])
        else:
            v=False
        i=i+1
    return lista2