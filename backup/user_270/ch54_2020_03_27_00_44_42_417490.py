def calcula_fibonnacci(n):
    k = 0
    lista = []
    soma = 1
    while k < n:
        lista.append(soma)
        soma += soma
        k += 1
    return lista
        
        