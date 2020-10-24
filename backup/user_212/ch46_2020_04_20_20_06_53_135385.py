def numero_no_indice(lista):
    i=0
    indice=[]
    while i<len(lista):
        if lista[i] == i:
            indice.append(i)
            i+=1
        else:
            i+=1
    return (indice)
            