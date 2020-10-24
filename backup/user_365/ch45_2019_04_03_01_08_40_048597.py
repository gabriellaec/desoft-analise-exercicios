def zera_negativos(lista):
    i=0
    lista2=[]
    while i<len(lista):
        if lista[i]<0:
            lista[i]==0
        	lista2.append(lista[i])
        	i+=1
        else:
            lista.append(lista[i])
            i+=1
        return lista2