def estritamente_crescente(x):
    a = [0]
    if x == []:
        return x
    a[0] = x[0]
    maior_numero = x[0]
    i=1
    while i<len(x):
        if x[1] > maior_numero:
            a.append(x[1])
            maior_numero = x[1]
        i+=1
    return a
    