def calcula_pi(n):
    i=0
    x=0
    while i<n:
        x+=6/(n**2)
        i+=1
    y=x**(1/2)
    return y