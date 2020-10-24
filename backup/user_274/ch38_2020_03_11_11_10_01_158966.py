def quantos_uns(num):
    tam=len(str(num))
    i=0
    c=0
    
    while i < tam:
        if num[i] == "1":
            c=c+1
        i=i+1
    return c