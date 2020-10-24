def soma_impares(lista):
    soma=0
    i=0
    lista_soma=[]
    while i<len(lista):
        if lista[i]/2 > 0:
            lista_soma.append(lista[i])
        	soma += lista[i]
        i+=1
    return soma