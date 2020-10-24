def calcula_fibonacci(n):
    i = 0
    lista = [0]*n
    lista[0] = 1
    if n == 1:
        return lista
    elif n == 2:
        lista[1] = 1
        return lista
    lista[1] = 1
    while (i+2)<n:
        lista[i+2] = lista[i+1] + lista[i]
