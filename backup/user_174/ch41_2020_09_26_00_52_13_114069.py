def zera_negativos(lista):
    lista=[-2,-3,0,-2]
    i=0
    while i<len(lista):
        if lista[i]<0:
            lista[i]=0
            i+=1
    print(lista)