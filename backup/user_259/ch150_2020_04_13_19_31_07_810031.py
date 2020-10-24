def calcula_pi(n):
    radicando = 0 
    for i in range(1,n+1):
        radicando+=6/(i**2)
    pi = radicando**0.5
    return pi