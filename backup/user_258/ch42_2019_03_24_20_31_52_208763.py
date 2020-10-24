def quantos_uns(num):
    a=str(num)
    c=0
    i=0
    while i<len(a):
        if a[i]=='1':
            c+=1
        i+=1
    return c

    