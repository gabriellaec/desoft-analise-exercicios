def numero_no_indice(lista):
    lista1=[]
    for i in range(len(lista)):
        y=lista[i]
        if y==i:
            c=i
            lista1.append(c)
    return lista1
        