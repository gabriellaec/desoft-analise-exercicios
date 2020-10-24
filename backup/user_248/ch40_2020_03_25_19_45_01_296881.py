def soma_valores(x, lista):
    i = 0
    while i < len(lista):
        if lista[i] == x:
            return i
        i += 1
    lista.append(x)
    return len(lista)-1