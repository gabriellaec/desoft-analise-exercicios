def numero_no_indice(lista):
    i=0    
    listaB=[]
    while i<len(lista):
        if i==lista[i]:
            listaB.append(lista[i])
        i+=1
    return listaB