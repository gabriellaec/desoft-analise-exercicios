def calcula_fibonacci(numero):
    if numero == 0:
        return [1]
    elif numero == 1:
        return [1, 1]
    else:
    	lista_fibonacci = [0] * numero
    	lista_fibonacci[0] = 1
    	lista_fibonacci[1] = 1
    	contador = 2
    	while contador < numero + 1:
        	lista_fibonacci.append(lista_fibonacci[contador - 1] + lista_fibonacci[contador - 2])
        	contador += 1
    	return lista_fibonacci