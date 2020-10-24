def raiz_quadrada(n): 
    if n==0:
        return 0
    if n==1:
        return 1
    i=0
    while i<n:
        max=1
        if n>max:
            max+=2
            i+=1
        else:
            i+=1
    x=n-max
    return x
    
        