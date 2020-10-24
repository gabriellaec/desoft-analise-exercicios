def quantos_uns(n):
    t=str(n)
    s=0
    i=0
    while i<len(t):
        if t[i]=='1':
            s+=1
        i+=1
    return s
     