def raiz_quadrada(n):
    i=0
    impar[0]=1
    impar[i]=impar[i]+2
    while n!=0:
        n-=impar[i]
    else:
        return i+1