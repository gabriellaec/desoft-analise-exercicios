def numero_no_indice(lista):
    lista1=[]
    i=0
    while i<len(lista):
        if lista[i]=='i':
            lista1.append(i)
        i+=1
    return lista1