def raiz_quadrada(n): 
    if n==0:
        return 0
    while True:
        max=1
        if n>max:
            max+=2
        else:
            break
    x=n-max
    return n-max
    
        