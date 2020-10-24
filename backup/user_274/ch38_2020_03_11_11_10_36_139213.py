def quantos_uns(num):
    n=str(num)
    tam=len(n)
    i=0
    c=0
    
    while i < tam:
        if n[i] == "1":
            c=c+1
        i=i+1
    return c