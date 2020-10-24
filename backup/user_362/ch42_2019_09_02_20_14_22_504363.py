def quantos_uns(x): 
    t=0
    contador=0
    while t < len(str(x)):
        if x[t] == "1":
            contador+=1
        t+=1
    return cont