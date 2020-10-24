def calcula_pi(n):
    s=0
    x=0
    for i in range(n):
        s+=6/i**2
    x=s**0.5
    return x
        