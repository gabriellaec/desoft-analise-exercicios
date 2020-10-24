def estritamente_crescente(lista):
    if len(lista) == 0:
        return none
    result = []
    result.append(lista[0])
    n = 0
    while n < (len(lista) - 1):
        if lista[n + 1] > lista[n]:
            result.append(lista[n + 1])
        n += 1
    return result