def subtracao_de_listas(a, b):
    i = 0
    j = 0
    while i < len(a) - 1:
        while j < len(b) -1:
            if a[i] == b[j]:
                del a[i]
                j += 1
            i += 1
    return a