def quantos_uns(x):
    x = str(x)
    tamanho = len(x)
    i = 0
    a = 0
    while i < tamanho:
        if  x[i] == "1":
            a = a + 1
        i = i + 1
    return a