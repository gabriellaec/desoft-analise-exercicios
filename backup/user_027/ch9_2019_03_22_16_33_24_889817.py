def lista_sufixos(x):
    i = 0
    tam = len(x) - 1
    y = []*tam
    while i <= tam:
        y.append(x[i])
    	y += 1
    return y