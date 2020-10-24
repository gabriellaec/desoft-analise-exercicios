def calcula_pi(n):
    i=1
    x=0
    while i < n:
        x+=6/(i**2)
        i+=1
    pi=(x)**(1/2)
    return pi