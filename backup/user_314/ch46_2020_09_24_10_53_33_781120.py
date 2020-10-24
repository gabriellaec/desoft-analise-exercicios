def numero_no_indice (lista1):
    i=0
    lista2=[]
    
    while (i<len(lista1)):
    
        if(int(lista1[i])==i):
            lista2.append(i)
        i+=1

    return lista2