def  filtra_positivos(lista):
    i=0
    positivos=[]
    while(i<len(lista)):
        if(lista[i]<=0):
            positivos.remove(lista[i])
            i+=1
        return positivos
       