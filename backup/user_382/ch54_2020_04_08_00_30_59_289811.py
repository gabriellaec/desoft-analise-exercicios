def calcula_fibonacci(n):
    lista = [1,1]
    if n <= 2:
        return lista
    for i in range(n-2):
        lista[i+2] = lista[i+1] + lista[i]
    return lista

