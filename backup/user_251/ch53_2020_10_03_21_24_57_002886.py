def soma_impares(a):
    i = 0
    resultado = 0
    while i < len(a):
        if a[i] % 2 != 0:
            resultado += a[i]
            i += 1
        else:
            i += 1
            
    return resultado