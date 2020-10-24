def calcula_fibonacci(n):
    lista = []
    n = len(lista)
    if n == 1:
        lista = [1]
        return lista
    elif n == 2:
        lista = [1,1]
        return lista
    i = 2
    while n>i:
        lista = [1,1]
        lista[i] = lista[i-1] + lista[i-2]
        i+=1
    return lista  