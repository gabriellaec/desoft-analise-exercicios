def verifica_progressao(lista):
    i = 0 
    pa = []
    pg = []
    while i < len(lista)-1:
        pa.append(lista[i+1] - lista[i])
        pg.append (lista[i+1] / lista[i])
        i+=1
    a = pa[0]
    k = 1
    x = True
    while x and k<len(pa):
        if pa[k] != a:
            x = False
        else:
            a = pa[k]
        k+=1
    b = pg[0]
    e = 1
    y = True
    while y and b<len(pg):
        if pg[e] != b:
            y = False
        else:
            b = pg[e]
        e += 1
    if x == True and y == True:
        return "AG"
    elif x == True:
        return "PA"
    elif y == True:
        return "PG" 
            