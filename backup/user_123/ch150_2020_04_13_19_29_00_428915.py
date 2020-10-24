def calcula_pi(n):
    i=1
    x=0
    while n > i-1 :
        x += 6/(i**2)
        i += 1 
    
    pi = x**0.5
    return pi