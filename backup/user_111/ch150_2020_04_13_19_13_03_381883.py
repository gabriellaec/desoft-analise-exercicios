def calcula_pi(n):
    i=0
    x=0
    while i<n-1:
        x+=6/((i+1)**2)
        i+=1
    y=x**(1/2)
    return y