def quantos_uns(numero):
    i=0
    x=0
    n = str(numero)
    while i < len(n):
        if n[i] == '1':
            x = x+1
        i = i+1
    return x
