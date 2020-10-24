def calcula_fibonacci (n):
    lista = []
    i = 0
    while i < n and i < 2:
        lista.append(1)
        i += 1
    while i < n:
        lista.append(lista[i-1] + lista[i-2])
        i+=1
    return lista
        