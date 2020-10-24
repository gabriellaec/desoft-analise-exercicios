
def subtracao_de_listas(a, b):
    c = a 
    i = 0
    while i < len(a):
        if a[i] in b:
            del c[i]
            i += 1
        else:
            i += 1
    return c



