def calcula_fibonacci(n):
    lista = [1,1]
    if n == 1:
        return lista[0]
    elif n > 1:
        i = 2
        while i < n:
            x = lista[i - 1] + lista[i - 2]
            lista.append(x)
            i += 1
        return lista