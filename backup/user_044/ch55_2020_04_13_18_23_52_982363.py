def encontra_maximo(matriz):
    lista=[]
    i=0
    while i<3:
        lista+=matriz[i]
        i+=1
    if lista[0]<0:
        lista[0]=-lista[0]
    maior=lista[0]
    i=1
    while i<9:
        if lista[i]<0:
            lista[i]=-lista[i]
        if lista[i]>maior:
            maior=lista[i]
            i+=1
        else:
            i+=1
    return maior
    