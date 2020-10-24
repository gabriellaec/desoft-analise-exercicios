def quantos_uns(x):
    t = 0
    cont = 0
    while t < len(str(x)):
        if x[t] == '1':
            cont += 1
        t += 1
    return cont