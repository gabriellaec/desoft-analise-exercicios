from math import factorial
def calcula_euler(n,x):
s = 0 
n = 100
x = 1
for i in range(n+1):
    s+=(x**i)/factorial(i)
return s
    