def quantos_uns(numero):
    i=0
    s=0
    a=str(numero)
    while i < len(a):
        if a[i]=="1":
            s+=1
        i+=1
    return s 