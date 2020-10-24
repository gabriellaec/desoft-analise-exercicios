def estritamente_crescente(lista):
    result = []
    result[0] = lista[0]
    n = 0
    while n < (len(lista) - 1):
        print(n)
        print(lista[n])
        if lista[n + 1] > lista[n]:
            result.append(lista[n + 1])
    
    return result
        