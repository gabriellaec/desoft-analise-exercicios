def numero_no_indice(lista):    
    listaB=[]
    for i in lista:
        if i==lista[i]:
            listaB.append(lista[i])
        i+=1
    return listaB