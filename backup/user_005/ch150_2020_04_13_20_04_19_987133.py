import math 
def calcula_pi(n):
    i = 1
    x = 0
    while i < len(n):
        x += 6/i**2
        i+=1
        return x