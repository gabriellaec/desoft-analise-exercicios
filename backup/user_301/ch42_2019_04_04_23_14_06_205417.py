def quantos_uns(numero):
    a=str(numero)
    i=0
    c=0	
    while i<len(numero):
        if a[i]=='1':
            c+=1
        i+=1
    return c
            