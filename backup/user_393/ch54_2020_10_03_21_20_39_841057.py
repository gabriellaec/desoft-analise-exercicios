def calcula_fibonacci(n):
    lista_fibonacci= [1,1]
    i= 2
    while i < n:
        lista_fibonacci.append(lista_fibonacci[i-1] + lista_fibonacci[i-2])
        i= i + 1
    return lista_fibonacci