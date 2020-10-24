def quantos_uns(n):
    n=str(n)
    c=0
    q=0
    for i in n:
        if i=='1':
            q+=1
    return(q)