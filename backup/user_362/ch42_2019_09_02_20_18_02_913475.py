def quantos_uns(x): 
    t=0
    contador=0
    sx = str(x)
    while t < len(sx):
        if sx[t] == "1":
            contador+=1
        t+=1
    return cont