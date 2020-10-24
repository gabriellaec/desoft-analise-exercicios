def numero_no_indice(numeros):
    i=0
    lista=[]
    while(i<len(numeros)):
        if(numeros[i]==i):
            lista.append(i)
        i+=1
        return lista
        