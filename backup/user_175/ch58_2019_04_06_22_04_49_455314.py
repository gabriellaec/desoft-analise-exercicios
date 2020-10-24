def calcula_fibonacci(n):
    x = n
    lista_fibonacci = [0]*x
    lista_fibonacci[0] = 1
    lista_fibonacci[1] = 1
    i = 2
    while i < x:
        lista_fibonacci[i] = lista_fibonacci[i-1] + lista_fibonacci[i-2]
        i += 1    
    return lista_fibonacci