def calcula_pi (n):
    i=1
    s=0
    pi=0
    while i<=n:
        s+=6/(i**2)
        i+=1
    pi=(s)**(1/2)
    return pi
    
        