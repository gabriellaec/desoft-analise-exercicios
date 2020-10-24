def soma_valores(lista):
    i = 0
    y = 0
    while i < len(lista):
        y += lista[i] + lista[i+1]
        i += 1
    return y