def raiz_quadrada(x):
    raiz=0
    impar=1
    while x!=0:
        x-=impar
        impar+=2
        raiz+=1
    return raiz