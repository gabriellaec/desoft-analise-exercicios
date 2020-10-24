def max_matrix(M):
    t = 0
    Max = max_lista(M[0])
    while t < len(M):
        if Max <= max_lista(M[t]):
            Max = max_lista(M[t])
        t += 1
    return Max