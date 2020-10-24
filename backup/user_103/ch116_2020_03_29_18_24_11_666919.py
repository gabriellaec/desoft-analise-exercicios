def raiz_quadrada(n):
    i=0
    impar[i]=impar[i]+2 
    impar[0]=1
    while n!=0:
        n-=impar[i]
    if n==0:
        return i+1
    