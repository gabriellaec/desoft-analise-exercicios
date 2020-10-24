def numero_no_indice(lista):
    lista2=[]
    i=0
    while i<len(lista)-1:
        if lista[i]==i:
            lista2[i]=i
        i+=1
    return lista2