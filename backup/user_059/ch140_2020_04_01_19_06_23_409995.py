def faixa_notas(lista):
    lnova = []
    i = 0
    x1 = 0 
    x2 = 0
    x3 = 0
    while i<len(lista):
        if lista[i]<5:
            x1=x1+1
        elif lista[i]>7:
            x3=x3+1
        else:
            x2=x2+1
        i+=1
    lnova.append(x1)
    lnova.append(x2)
    lnova.append(x3)
    return lnova