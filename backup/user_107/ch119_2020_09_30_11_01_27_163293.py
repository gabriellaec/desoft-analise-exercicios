import math

def calcula_euler (x, n):
    euler_power = 0
    
    for i in range(0, n):
        euler_power += x**i / math.factorial(i)
        
    return euler_power
