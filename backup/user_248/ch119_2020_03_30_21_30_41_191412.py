from math import factorial
s=0
n=3
for i in range(n+1):
    s+=i*x**i/factorial(i)
    return(s)