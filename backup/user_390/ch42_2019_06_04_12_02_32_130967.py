def quantos_uns(numero):
    n=0
    i=0
    while i< len(numero):
        if numero[i]==1:
            n+=1
            i+=1
        else:
            i+=1
    return n