def quantos_uns(numero): 
    t=0
    contador=0
    while t <= len(str(numero)):
        if numero[t] == "1":
            contador+=1
        t+=1
    return cont