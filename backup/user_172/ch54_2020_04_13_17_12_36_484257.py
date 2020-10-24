def calcula_fibonacci(n):
    lista = []
    n = len(lista)
    if n == 1:
        lista.append (1)
        return lista
    elif n == 2:
        lista.append (1,1)
        return lista
    i = 2
    while n>i:
        lista.append (1,1)
        lista[i] = lista[i-1] + lista[i-2]
        lista.append (lista[i])
        i+=1
    print (lista)
    return lista  