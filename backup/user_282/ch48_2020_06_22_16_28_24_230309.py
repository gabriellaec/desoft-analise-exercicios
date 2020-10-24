def eh_crescente(n):
    return all(i < j for i, j in zip(n, n[1:]))