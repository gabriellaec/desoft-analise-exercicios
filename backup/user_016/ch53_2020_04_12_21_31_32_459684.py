lista2 = []
def soma_impares(lista):
    i = 0
    while i < len(lista):
        if lista[i]%2 == 0:
            pass
        else:
            lista2.append(lista[i])
        i += 1
    return lista2