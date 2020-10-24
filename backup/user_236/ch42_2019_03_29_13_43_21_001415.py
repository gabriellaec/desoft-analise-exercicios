def quantos_uns(n):
    n=str(n)
    c=0
    q=0
    while c<len(n):
        if n[c]=='1':
            q+=1
        c+=1
    return(q)