def numero_no_indice(numeros):
    lista=[]
    i=0
    while(i<len(lista)):
        if(lista[i]==i):
            lista.append(i)
        i+=1
        return lista
        