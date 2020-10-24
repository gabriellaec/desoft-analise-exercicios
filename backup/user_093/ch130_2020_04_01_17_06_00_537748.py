def monta_mala(lista1):
    n=23
    i=0
    lista2=[]
    soma=0
    while i<len(lista1):
        soma=soma-lista1[i]
        if soma<=n:
            lista2.append(lista1[i])
        i+=1
    return lista2