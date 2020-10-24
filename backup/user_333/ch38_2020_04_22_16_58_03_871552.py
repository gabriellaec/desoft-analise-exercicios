def quantos_uns(n):
    n=str(n)
    i=0
    c=0
    for i in range(len(n)):
        if n[i]=='1':
            c+=1
    return c
        
print(quantos_uns(1030110641))