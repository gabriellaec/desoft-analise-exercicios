def calcula_pi(n):
    c=0
    for i in range(1, n+1):
        c = c + 6/(i**2)
        
    pi = (c)**.5
    return pi