def encontra_maximo(lista):
    i=0
    c=0
    a=lista[0][0]
    while i<len(lista):
        if lista[i][c]>a:
            a=lista[i][c]
        i+=1
        c+=1
        if c==2:
            c==0
    return a