n = 10000

def calcula_pi(n):
    i=1
    s=0
    while i < n-1:
        s += 6/(i**2)
        i+=1
    
    pi = s**0.5
    return pi

print(calcula_pi(n))