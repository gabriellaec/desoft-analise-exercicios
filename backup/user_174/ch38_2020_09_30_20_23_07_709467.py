def quantos_uns(lista):
    s=0
    i=0
    while s<len(str(lista)):
        if lista[i]==1:
            s=1*lista[i]
        s=s+1
    return (s)
    