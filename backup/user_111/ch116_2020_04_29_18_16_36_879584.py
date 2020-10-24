def raiz_quadrada(n):
    i=0
    a=1
    if n==1:
        return 1
    if n==0:
        return 0
    while a<=n:
        n-=a
        i+=1
        if n==0:
            return i
  
        a+=2