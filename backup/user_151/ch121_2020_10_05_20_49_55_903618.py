def subtracao_de_listas(a, b):
    i = 0
    j = 0
    k = 0
    c = []
    while i < len(a):
        if a[i] not in b:
            c.append(a[i])
            k += 1
            
        i += 1 
    return c  