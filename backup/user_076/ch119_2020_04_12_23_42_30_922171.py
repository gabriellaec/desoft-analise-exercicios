import math 

def calcula_euler (x,n):
    i = 0
    euler = 0
    while i<n:
        euler += (x**i)/math.factorial(i)
        i+=1
    return euler