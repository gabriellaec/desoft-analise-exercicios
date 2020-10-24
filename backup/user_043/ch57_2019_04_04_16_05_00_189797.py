def soma_impares(numeros):
    i=0
    soma=0
    while i<len(numeros):
        if numeros[i]%2==0:
            soma+=1
		i+=1
	return soma
            