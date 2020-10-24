def quantos_uns(p):
    f= str(p)
    a=0
    c=0
    while f[-1]>=f[a]:
        if f[a]=='1':
            c+=1
            a+=1
        else:
            a+=1
    return c