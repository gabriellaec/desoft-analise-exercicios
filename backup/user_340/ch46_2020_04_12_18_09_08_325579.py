def numero_no_indice(lista):
    lista1=[]
    for t in lista:
        if lista[t]==t:
            lista.append(t)
    return lista1