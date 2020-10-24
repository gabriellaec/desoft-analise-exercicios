def modulo(n):
    if n<0:
        return n*-1
    else:
        return n

def encontra_maximo(L):
    i=0
    n=0
    m=L[i+1][0]
    while i<3:
        j=1
        while j<3:
            a=L[i][j]
            b=L[i][j-1]
            if modulo(a)>modulo(b):
                n=L[i][j]
            j+=1
        if n<modulo(m):
            n=m
        i+=1
    return n