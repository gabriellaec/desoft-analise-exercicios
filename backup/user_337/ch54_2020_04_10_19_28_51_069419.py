def calcula_fibonacci(n):
    lista = []
    lista.append(1)
    lista.append(1)
    i = 0
    while len(lista)<n:
        x = lista[i]+lista[i+2]
        lista.append(x)
        i+=1
    return lista