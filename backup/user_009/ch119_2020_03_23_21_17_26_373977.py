import math
def calcula_euler(x,n):
    sum1 = 1
    for i in range(1,n+1):
        sum1=sum1+(1/math.factorial(i))
    return sum1