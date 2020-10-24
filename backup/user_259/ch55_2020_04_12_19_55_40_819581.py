def encontra_maximo(lista):
    max = 0
    i = 0
    while i<len(lista):
        for j in lista[i]:
            if j>max:
                max = j
        i+=1
    return max