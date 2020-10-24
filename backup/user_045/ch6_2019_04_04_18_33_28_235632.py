def encontra_maximo(m):
    l=0
    
    s=0
    
    while l<len(m):
        c=0
        while c<len(m[l]):
            m[l][c]=(m[l][c]**2)**0.5
            if s<m[l][c]:
                s=m[l][c]
            c+=1
        
        l+=1
    return s
