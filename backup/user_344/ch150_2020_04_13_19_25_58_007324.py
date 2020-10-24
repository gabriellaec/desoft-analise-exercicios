def calcula_pi(n):
    i=1
    soma=0
    while i-1 < n:
        soma+=6/(i**2)
        i+=1
        pi = soma**0.5
    return pi
