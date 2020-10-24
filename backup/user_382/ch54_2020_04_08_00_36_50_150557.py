def calcula_fibonacci(n):
    if n == 2:
        return [1,1]
    if n == 1:
        return [1]
    if n == 0:
        return []
    lista = [1,1]
    for i in range(2,n):
        lista.append(lista[i-2] + lista[i-1])
    return lista
