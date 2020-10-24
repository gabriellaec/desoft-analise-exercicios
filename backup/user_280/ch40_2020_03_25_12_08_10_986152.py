def soma_valores(a):
    num_elementos = len(a)
    i = 0
    s = 0
    while i<num_elementos:
        s += a[i]
        i += 1
    return s