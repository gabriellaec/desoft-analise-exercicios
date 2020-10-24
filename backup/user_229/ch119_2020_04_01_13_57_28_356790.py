import math
x = int(input("Valor de x: "))
n = int(input("Valor de n: "))
i = 0
s = 0
for i in range(n+1):
   s += (x**i)/math.factorial(i)
   print(s)