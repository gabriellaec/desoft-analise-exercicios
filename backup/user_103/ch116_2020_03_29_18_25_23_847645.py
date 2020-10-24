def raiz_quadrada(n):
    i=0
    impar[0]=1
    impar=impar[i]+2 
    while n!=0:
        n-=impar[i]
        i+=1
    if n==0:
        return i+1
    