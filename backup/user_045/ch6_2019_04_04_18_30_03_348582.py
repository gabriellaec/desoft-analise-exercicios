def encontra_maximo(m):
    l=0
    
    s=0
    ma=[]
    while l<len(m):
        c=0
        while c<len(m[l]):
            m[l][c]=(m[l][c]**2)**0.5
            if m[l][c]>0:
                s=m[l][c]
            c+=1
        ma.append(s)
        l+=1
    return ma