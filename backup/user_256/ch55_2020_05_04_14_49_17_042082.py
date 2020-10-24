def encontra_maximo(lista):
    max = 0
    i = 0 
    while i < len(lista):
        for e in lista(i):
            if e>max:
                max = e
        i+=1
    return max
