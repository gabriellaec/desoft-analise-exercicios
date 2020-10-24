def verifica_quadrado_perfeito (N):
    M = N
    i = 0
    while M > 0:
        M = M - i * 2
        i = i + 1
    if M**2 == N:
        return True
    else:
        return False