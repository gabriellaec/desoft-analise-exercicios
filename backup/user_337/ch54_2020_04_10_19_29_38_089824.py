def calcula_fibonacci(n):
    lista = []
    lista.append(1)
    if n == 1:
        return lista
    lista.append(1)
    if n == 2:
        return lista
    i = 0
    while len(lista)<n:
        x = lista[i]+lista[i+1]
        lista.append(x)
        i+=1
    return lista