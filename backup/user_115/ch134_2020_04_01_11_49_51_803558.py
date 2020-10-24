def verifica_quadrado_perfeito(n):
    m = n
    count = 0
    while (m >= 0):
        m = m - 2*count
        count += 1
    return bool((m**2 == n))