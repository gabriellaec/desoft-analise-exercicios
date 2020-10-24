import math
k = 1
i = 0
def calcula_euler(x,n):
    r = 0
    while x<n:
        y = 1 + x +((x**(k+1)/(math.factorial(i+1)))*n)
        r +=1
        return y
print(calcula_euler(2,2))