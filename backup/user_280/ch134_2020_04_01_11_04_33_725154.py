def verifica_quadrado_perfeito(n):
    numeros_pares = []
    numeros_pares[0] = 2
    i=0
    while i < len(numeros_pares):
        numeros_pares[i+1] = numeros_pares[i] + 2
        i += 1
    m = n
    j=0
    while m > 0:
        m -= numeros_pares[j]
        j += 1
    m -= numeros_pares[j]
    if m*m == n:
        return True
    else:
        return False
