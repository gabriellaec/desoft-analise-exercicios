def quantos_uns(numero):
    i=0
    y=0
    w = str(numero)
    x = w[i]
    while i<len(w):
        if x == "1":
            y+=1
            i+=1
        else:
            i+=1
    return y