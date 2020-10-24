def calcula_pi(n):
    i=1
    s=0
    while i-1 < n:
        s += 6/(i**2)
        i+=1
    pi = s**0.5
    return pi