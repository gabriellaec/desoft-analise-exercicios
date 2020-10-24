def calcula_fibonacci(n):
    lista = [1, 1]
    i = 2
    if n == 1:
        lista = [1]
    elif n == 2:
        lista = lista
    else:
        lista = [1, 1]
        while i < n:
            novo_elemento = lista[i-1] + lista[i-2]
            lista.append(novo_elemento)
            i += 1
    return lista
        