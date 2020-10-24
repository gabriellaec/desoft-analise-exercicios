def numero_no_indice(lista):
    lista1=[]
    for t in lista:
        if lista[t]==t:
            lista1.append(t)
    return lista1