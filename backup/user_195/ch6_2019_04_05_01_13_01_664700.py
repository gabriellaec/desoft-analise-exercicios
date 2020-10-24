def modulo(n):
    if n>0:
        return n
    else:
        return -n

def encontra_maximo(L):
    i=0
    maior=0
    while i<3:
        j=0
        while j<3:
            a=modulo(L[i][j])
            if a>maior:
                maior=a
            j+=1
        i+=1
    return maior