def numero_no_indice(lista):
    if lista == []:
        return []
    else:
    lista2=[]
    i=0
    while i<len(lista):
        if lista[i]==i:
            lista2[i]=i
        i+=1
    return lista2