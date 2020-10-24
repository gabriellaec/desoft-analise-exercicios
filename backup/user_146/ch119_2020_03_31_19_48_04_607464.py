import math
k = 1
i = 1
x = 0
while x < n:
def calcula_euler(x,n):
    y = 1 + x +((x**(k+1)/(math.factorial(i+1)))*n)
    x +=1
    return y
print(calcula_euler(10,20))