def soma_impares (numeros):
    primo = False
    s = 0 
    i = 0
    while i < len(numeros):
        if numeros[i] % 2 == 0:
            primo = False
        if primo == True:
            s += numero[i]
        i += 1
    return s          