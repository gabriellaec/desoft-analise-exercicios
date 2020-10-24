def numero_no_indice(x):
    a = []
    i = 0
    while i < len(x):
            if x[i] == i:
                a.append(x[i])
            i+=1
    return a
            