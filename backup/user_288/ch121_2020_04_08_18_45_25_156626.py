def subtracao_de_listas(x,y):
    u=0
    i=0
    casas=0
    while i < len(x):
        if u < len(y):
            if x[i] != y [u]:
                u += 1
            elif x[i] == y [u]:
                del x[i]
                u = 0
                c=len(x)
        else:
            u = 0
            i += 0
    return x
            
