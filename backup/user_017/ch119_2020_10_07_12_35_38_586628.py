import math
def calcula_euler(x,n):
s=0
i=0
while i<n:
    s+=(x**i)/math.factorial(x)
    i+=1
    