def encontra_maximo(lista):
    i=1
    c=0
    a=lista[0][0]
    while i<len(lista):
        while c<=2:
            if lista[i][c]>a:
                a=lista[i][c]
                continue
            c+=1
            if c>=2:
                c==0
                continue
        i+=1
    return a
lista=[[311, 211, 321], [511,12,11], [8,9,110]]
print(encontra_maximo(lista))