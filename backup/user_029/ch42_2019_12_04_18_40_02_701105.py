def quantos_uns(x):
    x = str(x)
    contador = 0
    for i in x:
        if x[i] == "1":
            contador += 1
    return contador