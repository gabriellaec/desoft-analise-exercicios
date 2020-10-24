def junta_nome_sobrenome(a, b):
    i = 0
    r = [0]*len(a)
    while i < len(a):
        r[i] = a[i] + " " + b[i]
        i = i + 1
    return r