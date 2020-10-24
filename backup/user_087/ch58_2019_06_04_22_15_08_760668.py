def calcula_fibonacci(n):
    lista = [1, 1]
    i = 2
    if n == 2:
        lista = lista
    else:
    	while i < n:
       		lista[i] = lista[i-1] + lista[i-2]
        	i += 1
    return lista
        