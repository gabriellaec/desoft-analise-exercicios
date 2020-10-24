def filtra_positivos(lista):
    listap=[]
    i=0

    while(i<len(lista)):
        if(lista[i]>0):
            listap.append(lista[i])  
        i+=1

    return listap