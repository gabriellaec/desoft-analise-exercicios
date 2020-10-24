def  filtra_positivos(lista):
    i=0
    while(i<len(lista)):
        if(lista[i]>0):
            lista.append(lista[i])
            i+=1
        return lista
       