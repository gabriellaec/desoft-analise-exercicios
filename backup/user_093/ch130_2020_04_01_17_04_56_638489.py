def montar_mala(lista1):
    n=23
    lista2=[lista1[i]]
    i=0
    soma=0
    while i<len(lista):
        soma=soma-lista1[i]
        if soma<=n:
            lista2.append(lista1[i])
        i+=1
    return lista2