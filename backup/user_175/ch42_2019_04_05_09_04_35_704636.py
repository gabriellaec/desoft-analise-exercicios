def quantos_uns(x):
    t = 0
    cont = 0
    while t < len(str(x)):
        if x[t] == '1':
            cont += 1
        t += 1
    return cont


def lista_sufixos(x):
    x = str(x)
    cont = 0
    while cont < len(x):
        if x[cont] == ' ':
            cont +=1
        else:
            y[cont] = x[cont]
            cont += 1
    return list(x)