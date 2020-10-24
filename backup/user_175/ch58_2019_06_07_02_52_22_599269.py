def calcula_fibonacci(n):
    if n == 0:
        lista = []
    elif n == 1:
        lista = [1]
    elif n == 2:
        lista = [1,1]
    else:
        lista = 2*[0]
        lista[0] = 1
        lista[1] = 1
        i = 2
        while i < n:
            x = lista[i-1] + lista[i-2]
            lista.append(x)
            i += 1
    return lista