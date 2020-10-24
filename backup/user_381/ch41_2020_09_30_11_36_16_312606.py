def zera_negativos(n):
    i =  0
    tamanho = len(n)
    while i < tamanho:
        if n[i] < 0:
            n[i] = 0
    i = i + 1
    return n