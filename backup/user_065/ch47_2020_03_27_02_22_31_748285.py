def estritamente_crescente(lista):
    result = []
        if len(lista) == 0:
        return result
    result.append(lista[0])
    n = 0
	print(lista)
    while n < (len(lista) - 1):
        if lista[n + 1] > lista[n]:
            if lista[n+1] > result[n - 1]:
                result.append(lista[n + 1])
        n += 1
    return result