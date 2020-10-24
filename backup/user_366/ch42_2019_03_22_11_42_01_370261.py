def quantos_uns(n):
    i = 0
    s = 0
    a = str(n)
    while i < len(a):
        if a[i] == '1':
            s += 1
        i += 1
    return s