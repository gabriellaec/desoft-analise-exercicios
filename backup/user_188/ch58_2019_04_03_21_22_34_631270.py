def calcula_fibonacci(numero):
    if numero == 0:
        lista_fibonacci = [1]
        return lista_fibonacci
    elif numero == 1:
        lista_fibonacci = [1] * 2
        return lista_fibonacci
    else:
    	lista_fibonacci = [0] * numero
    	lista_fibonacci[0] = 1
    	lista_fibonacci[1] = 1
    	contador = 2
    	while contador < numero + 1:
        	lista_fibonacci[numero] = lista_fibonacci[contador - 1] + lista_fibonacci[contador - 2]
        	contador += 1
    	return lista_fibonacci