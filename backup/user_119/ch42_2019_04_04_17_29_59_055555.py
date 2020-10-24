def quantos_uns(n):
    cont=0
    i=0
    while i<len(n):
        if n[i]=='1':
            cont+=1
        i+=1
    return cont
print (quantos_uns(n))