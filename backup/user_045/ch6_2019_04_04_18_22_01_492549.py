def encontra_maximo(m):
    l=0
    c=0
    s=0
    ma=[]
    while l<len(m):
        while c<len(m[l]):
            m[l][c]=(m[l][c]**2)**0.5
            s=s+m[l][c]
            c+=1
        ma[l]=s
        l+=1
    return ma
        