def modulo(n):
    if n<0:
        return n*-1
    else:
        return n
    
    
def encontra_maximo(L):
    X=[]
    i=0
    n=0
    z=1
    t=0
    while n<3:
        j=0
        while j<3:
            g=modulo(L[i][j])
            X.append(g)
            j+=1
        n+=1
    while z<9:
        if X[z]>X[z-1]:
            t=X[z]
        z+=1
    return t
            