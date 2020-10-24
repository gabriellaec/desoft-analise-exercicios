def encontra_maximo(lista):
    i=0
    c=0
    a=lista[0][0]
    while i<len(lista):
        while c<=2:
            if abs(lista[i][c])>a:
                a=abs(lista[i][c])
            c+=1
        c=0
        i+=1
    return a