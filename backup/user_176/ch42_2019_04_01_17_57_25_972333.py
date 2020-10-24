def quantos_uns(n):
    a= str(n)
    c= 0
    i= 0
    while i<len(a):
        if a[i]=='1':
            c+=1
        i+=1
    return c