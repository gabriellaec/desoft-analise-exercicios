def estritamente_crecente(lista1):
    lista2=[lista1[0]]
    v=True
    i=0
    while i<len(lista1) and v=True:
        if lista[i]<lista[i+1]:
            lista2.append(lista[i])
        else:
            v=False
        i=i+1
    return lista2