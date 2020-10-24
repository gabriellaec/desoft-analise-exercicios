import math
def fatorial(n):
    i = 1
    while i <= n:
        n *= i
        i += 1
print(fatorial(5))