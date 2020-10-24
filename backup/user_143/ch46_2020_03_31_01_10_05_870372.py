def numero_no_indice(lista):
    i=0
    lista1=[]
    while i<len(lista):
        y=lista[i]
        if y==i:
            c=i
            lista1.append(c)
            i+=1
        else:
            i+=1
    return lista1
        