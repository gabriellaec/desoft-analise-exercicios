def calcula_fibonacci(n):
    lista, i = [1,1], 2
    while i <= n:
        lista[i+2] = lista[i] + lista[i+1]
        i -=1
    return lista