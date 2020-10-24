def estritamente_crescente(lista):
    result = []
    test = 0
    i = 0
    
    while i < len(lista):
        if i == 0:
            result.append(lista[i])
            test = lista[i]
        else:
            if lista[i] > test:
                result.append(lista[i])
                test = lista[i]
        i = i + 1
    return result