def quantos_uns(numero):
    i=0
    x=0
    n = str(numero)
    while i < len(n) + 1:
        if n[i] == 1:
            x+=1
        i+=1
    return x