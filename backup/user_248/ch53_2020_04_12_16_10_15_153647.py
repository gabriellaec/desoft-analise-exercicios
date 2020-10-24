def soma_impares(lista):
    s = 0
    i = 1
    while i < len(lista):
        if i % 2:  
            s += i
            i += 1
    return s