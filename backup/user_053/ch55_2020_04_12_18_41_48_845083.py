def max_lista(lista):
    i = 0
    maximo = lista[0]
    # Compara e verifica o maior da lista
    while i < len(lista):
        if maximo <= lista[i]:
            maximo = lista[i]
        i = i + 1
    return maximo

def encontra_maximo(matriz):
    i = 0
    Max = max_lista(matriz[0])
    while i < len(matriz):
        if Max <= max_lista(matriz[i]):
            Max = max_lista(matriz[i])
        i += 1
    return Max