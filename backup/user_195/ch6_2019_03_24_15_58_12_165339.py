def modulo(n):
    if n<0:
        return n*-1
    else:
        return n

def encontra_maximo(L):
    i=0
    n=0
    m=modulo(L[i+1][0])
    while i<3:
        j=1
        while j<3:
            a=modulo(L[i][j])
            b=modulo(L[i][j-1])
            if a>b:
                n=L[i][j]
            j+=1
        if n<m:
            n=m
        i+=1
    return n