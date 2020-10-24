def raiz_quadrada(n):
    a=1
    if n==1:
        return True
    if n==0:
        return True
    while a<=n:
        n-=a
        if n==0:
            return True 
        elif n<0:
            return False
        a+=2
    