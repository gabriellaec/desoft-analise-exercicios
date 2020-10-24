def calcula_fibonacci(n):
    lista_fibonacci=[1]*n
    i=2
    while i<n:
        lista_fibonacci[i]=lista_fibonacci[i-1]+lista_fibonacci[i-2]
        i+=1
    return lista_fibonacci