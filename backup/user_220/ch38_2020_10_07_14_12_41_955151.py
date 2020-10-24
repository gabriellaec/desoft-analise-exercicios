def quantos_uns(numero):
    i=0
    y=0
    w = str(numero)
    while i<len(w):
        x = w[i]
        if x == "1":
            y+=1
            i+=1
        else:
            i+=1
    return y