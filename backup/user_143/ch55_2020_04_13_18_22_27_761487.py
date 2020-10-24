def encontra_maximo(matriz):
    a=0
    lista=[]
    while a<3:
        b=0
        lista+=matriz[a]
        a+=1
    maior=lista[0]
    if maior<0:
        maior=-lista[0]
    i=1
    while i<9:
        c=lista[i]
        if c<0:
            c=-lista[i]
        if c>maior:
            maior=c
            i+=1
        else:
            i+=1
    return maior
        
        