def quantos_uns(numero):
    i=0
    n=0
    while i<len(numero):
        if numero[i]==1:
            n=n+1
            i+=1
        else:
            i+=1
    return n