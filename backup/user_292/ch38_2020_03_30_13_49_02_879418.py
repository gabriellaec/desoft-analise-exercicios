def quantos_uns(n):
    f=str(n)
    a=0
    c=0
    b=len(f)
    while a<b:
        if f[a]=='1':
            c+=1
            a+=1
        else:
            a+=1
    return c