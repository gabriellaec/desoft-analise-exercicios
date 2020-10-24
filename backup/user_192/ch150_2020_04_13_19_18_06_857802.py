import math
def calcula_pi(n):
    pi = [0]*n
    i=0
    while i<n:
        pi[i] = (6/(i+1)**2)
        i+=1
    y = math.sqrt(sum(pi))
    return y
    