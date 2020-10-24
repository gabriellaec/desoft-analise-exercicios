def calcula_fibonacci (n):
    lista = [0]*n
    lista[0] = 1
    lista[1] = 1
    i = 2
    while i < n:
        a = lista[i-1] + lista[i-2]
        lista.append(a)
        i+=1
    return lista2
        