def zera_negativos(lista_numeros):
    cont=0
    while cont<len(lista_numeros):
    	if lista_numeros[cont]<0:
            lista_numeros[cont]=0
    	cont+=1
    return lista_numeros