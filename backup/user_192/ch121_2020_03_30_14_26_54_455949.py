def subtracao_de_listas(a, b):
    i = 0
    j = 0
    while i < len(a):
        while j < len(b):
            if a[i] == b[j]:
                del a[i]
                i-= 1
            j += 1
        i += 1
    return a