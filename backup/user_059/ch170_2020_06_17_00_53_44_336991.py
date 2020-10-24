def apaga_repetidos(x):
    l = []
    for i in range(len(x)):
        if x[i] not in l:
            l.append(x[i])
        else:
            l.append('*')
    y = "".join(l)
    return y 
