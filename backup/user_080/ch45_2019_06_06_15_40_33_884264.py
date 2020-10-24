def zera_negativos(lista):
    i=0
    while lista[i]>-1:
        if lista[i]<0:
            lista[i]=0
        else:
            i+=1
	return lista
        
        
    