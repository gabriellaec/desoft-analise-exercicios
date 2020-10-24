import math
def calcula_pi(n):
    pi = [0]*n
    i=0
    while i<n:
        pi[i] = math.sqrt(6/(math.factorial(n+1))**2)
        i+=1
    y = sum(pi)
    return y
    