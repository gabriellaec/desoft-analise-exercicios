def encontra maximo(m):
    l=0
    c=0
    s=0
    while l<len(m):
        while c<len(m[l]):
            ma[l][c]=(m[l][c]**2)**0.5
            c+=1
        l+=1
    return ma
        