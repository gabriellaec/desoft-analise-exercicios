def quantos_uns(x):
    x = ""
    contador = 0
    for i in range(1,len(x)):
        if x[i] == "1":
            contador += 1
    return contador