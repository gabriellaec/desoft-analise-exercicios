def raiz_quadrada(n):
    i=1
    j=0
    while n!=0:
        n=n-i
        i+=2
        j+=1
    return j