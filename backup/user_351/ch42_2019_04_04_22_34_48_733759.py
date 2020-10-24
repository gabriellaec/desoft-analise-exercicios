def quantos_uns(numero):
    i = 0
    contador=0
    y = str(numero)
    while i < len(y):
        if y[i]=="1":
            contador+=1
        i+=1
    return contador