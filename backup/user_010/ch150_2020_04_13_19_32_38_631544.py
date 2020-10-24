def calcula_pi (n):
    s=0
    for i in range (1,n+1):
        e=6/(i**2)
        s+=e
    pi=s**(1/2)
    return pi