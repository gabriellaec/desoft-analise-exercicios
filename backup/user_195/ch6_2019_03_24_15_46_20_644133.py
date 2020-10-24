def encontra_maximo(L):
    i=0
    n=0
    m=L[i+1][0]
    while i<3:
        j=1
        while j<3:
            if L[i][j]>L[i][j-1]:
                n=L[i][j]
            j+=1
        if n<m:
            n=m
        i+=1
    return n
            