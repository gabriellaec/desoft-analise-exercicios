def numero_no_indice(numeros):
    lista=[]
    i=0
    while(i<len(numeros)):
        if(numeros[i]==[i]):
            lista.append(numeros[i])
        i+=1
        return lista
        