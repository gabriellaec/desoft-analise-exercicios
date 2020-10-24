def calcula_fibonacci(n):
    lista_fibonacci = [0]*n
    lista_fibonacci[0] = 1
    lista_fibonacci[1] = 1
    i = 2
    while i < n:
        lista_fibonacci[i] = lista_fibonacci[i-1] + lista_fibonacci[i-2]
        i += 1    
    soma = 0
    x = 0
    while x < len(lista_fibonacci):
        soma += lista_fibonacci[x]
        x += 1
    return soma