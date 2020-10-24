def verifica_quadrado_perfeito (n):
    i=1
    m = n
    while m>=0:
        delta = 2*i
        m -= delta
        i += 1
    resultado = (m**2 == n)
    return resultado

print (verifica_quadrado_perfeito(9))

    