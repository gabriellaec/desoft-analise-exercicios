def calcula_fibonacci(n):
    lista = [0]*n
    if len(lista) == 0:
        return lista
    elif len(lista) == 1:
        lista[0]= 1
        return lista
    else:
        lista[0]= 1
        lista[1] = 1
        i=2
        while i != n:
            lista[i]= lista[i-1] + lista[i-2]
            i += 1
        return lista