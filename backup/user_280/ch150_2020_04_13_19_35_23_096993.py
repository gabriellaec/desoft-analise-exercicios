import math
def calcula_pi(n):
    a = [0]*n
    i = 0
    while i < n:
        a[i] = 6/(i+1)**2
        i+=1
    y = sum(a)
    return math.sqrt(y)
    