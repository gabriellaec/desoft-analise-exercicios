def subtracao_de_listas(a,b):
    i1 = 0
    c = a
    while i < len(a):
        if a[i] in b:
            del c[i]
        i += 1
    return c
