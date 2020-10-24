def numero_no_indice(lista):
    lista2=[]
    i=0
    while i<len(lista):
        if lista[i]==i:
            lista2[i]=1
        i+=1
    return lista2