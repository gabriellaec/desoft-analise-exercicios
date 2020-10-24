def calcula_pi(n):
    s=0
    for i in range(n):
        s+=6/(i+1)**2
    x=s**0.5
    return x
        