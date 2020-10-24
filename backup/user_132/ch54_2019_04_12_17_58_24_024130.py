def junta_nome_sobrenome(a, b):
    i = 0
    r = []*len(a)
    while i < len(a):
        r[i] = a[i] + " " + b[i]
        i = i + 1
    return r