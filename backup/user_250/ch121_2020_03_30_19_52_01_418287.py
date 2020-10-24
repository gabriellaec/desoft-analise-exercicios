def subtracao_de_listas(a,b):
    l3 = []
    i1 = 0
    while i < len(a):
        if a[i] in b:
            del a[i]
        i+=1
    return a
