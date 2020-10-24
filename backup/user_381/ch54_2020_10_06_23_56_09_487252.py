def calcula_fibonacci(n):
    if n == 0:
        lista_fibonacci = []
    if n == 1:
        lista_fibonacci = [1]
    if n > 1:
        lista_fibonacci = [0]*n
        lista_fibonacci[0] = 1
        lista_fibonacci[1] = 1
        i = 2
        while i < len(lista_fibonacci):
            lista_fibonacci[i] = lista_fibonacci[i-1] + lista_fibonacci[i-2]
            i += 1
    return lista_fibonacci 