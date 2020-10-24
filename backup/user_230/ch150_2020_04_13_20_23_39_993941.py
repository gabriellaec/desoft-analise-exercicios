def calcula_pi(n):
    x=0
    for i in range(1, n):
        x+=6/(i**2)
    pi=x**(1/2)
    return pi
