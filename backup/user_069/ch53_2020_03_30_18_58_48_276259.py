def soma_impares (numeros):
    s = 0 
    i = 0
    while i < len(numeros):
        if numeros[i] % 2 != 0 and numeros[i] != 2:
            s += numeros[i]
        i += 1
    return s          