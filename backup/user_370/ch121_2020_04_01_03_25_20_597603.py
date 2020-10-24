def subtracao_de_listas(x,y):
    u=0
    i=0
    b=len(y)
    c=len(x)
    casas=0
    while i<c:
        if u<b:
            if x[i]!=y[u]:
                u+=1
            elif x[i] == y[u]:
                del x[i]
                u=0
                c=len(x)