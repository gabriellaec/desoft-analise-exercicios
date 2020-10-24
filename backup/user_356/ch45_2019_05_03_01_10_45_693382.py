def zera_negativos(lista):
    i=0
    n=len(lista)
    lista_nova=[]
    while i<n:
        if lista[i]<0:
        	lista_nova.append(0)
        else:
            lista_nova.append(lista[i])
        i+=1
    return lista_nova