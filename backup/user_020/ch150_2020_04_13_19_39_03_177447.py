import math
def calcula_pi(n):
    i = 1
    while i<n:
        pi = math.sqrt(6/i**2)**n
        i += 1
        return pi
print(calcula_pi(10))