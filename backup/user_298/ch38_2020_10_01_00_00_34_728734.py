def quantos_uns(num):
    t = 0
    w =0
    a = str(num)
    while t < len(a):
        if a[t] == '1':
            w += 1
        t += 1
    return w 