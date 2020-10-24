def numero_no_indice(x):
    i = 0
    r = []
    for k in x:
        if x[i] == i:
            r.append(x[i])
        i = i + 1
    return r

x = [1, 3, 2, 4]

print (numero_no_indice(x))