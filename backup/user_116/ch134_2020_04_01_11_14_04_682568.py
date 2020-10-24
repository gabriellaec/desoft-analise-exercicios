def verifica_quadrado_perfeito(n):
    m=n
    i=2
    while m>=0 :
        if m>0:
            m-=i
            i+=2
        elif m ==0:
            m-=i
    if m**2==n:
        r=True
    else:
        r=False    
    return r 