import math
i = 0
s = 0
for i in range(n+1):
    s += (x**i)/math.factorial(i)
print(s)