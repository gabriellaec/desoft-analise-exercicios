def quantos_uns(p):
    f= str(p)
    a=0
    c=0
    b=len(p)
    while a<b:
        if f[a]=='1':
            c+=1
            a+=1
        else:
            a+=1
    return c