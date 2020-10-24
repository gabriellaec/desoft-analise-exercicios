def inverte_lista(a):
    i = len(a) - 1
    resultado = []
    while i >= 0:
        resultado.append(a[i])
        i -= 1
    return resultado