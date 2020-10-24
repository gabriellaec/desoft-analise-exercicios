def calcula_fibonacci (n):
    lista = [0]*n
    lista[0] = 1
    lista[1] = 1
    i = 2
    while i < n:
        lista[i]= f[i-1] + f[i-2]
        i+=1
    return lista
        