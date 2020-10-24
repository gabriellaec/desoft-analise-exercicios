def calcula_fibonacci(numero):
	numero -= 1
    if numero == -1:
        lista = []
    elif numero == 0:
        lista = [1]
    elif numero == 1:
        lista = [1,1]
    else:
        lista = [0] * 2
        lista[0] = 1
        lista[1] = 1
        contador = 1
        while contador < numero:
            lista.append(lista[numero] + lista[numero - 1])
            contador +=1
	return lista