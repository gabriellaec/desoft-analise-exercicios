def numero_no_indice(lista):
    i=0
    lista2=[]
    while i<len(lista):
        if i == lista[i]:
            lista2.append(lista[i])
        i+=1
    return lista2
            