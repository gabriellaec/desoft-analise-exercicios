def calcula_fibonnacci(n):
	lista = []
    k = 0
    soma = 1
    while k < n:
        lista.append(soma)
        soma += soma
        k += 1
    return lista
        
        