def estritamente_crescente(lista):
    result = []
    result.append(lista[0])
    print(lista)
    n = 0
    while n < (len(lista) - 1):
        if lista[n + 1] > lista[n]:
            result.append(lista[n + 1])
        n += 1
    return result