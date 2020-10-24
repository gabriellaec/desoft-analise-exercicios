def quantos_uns(x):
    tamanho = len(x)
    i = 0
    a = 0
    while i < tamanho:
        i = i + 1
        if  x[i-1] == "1":
            a = a + 1
    return a