def quantos_uns(n):
    cont=0
    i=0
    n=''
    while i<len(n):
        if n[i]=='1':
            cont+=1
        i+=1
    return cont
