import math
def calcula_pi(n):
    pi = 0.0
    for i in range(1,n):
        pi = pi + ((6 / i**2)*math.sqrt)
    return pi
        
