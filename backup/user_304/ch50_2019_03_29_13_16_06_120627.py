def numero_no_indice (lista):
    indice=[]
    i=0   
    while i<len(lista):
        if lista[i]==i:
            indice.append (i)
        i+=1
    return indice