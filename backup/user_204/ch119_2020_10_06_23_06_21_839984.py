import math
def calcula_euler(x,n):
    conta = 0
    i = 3
    while n >= i:
        conta = conta + (x ** i) / (math.factorial(i))
        i += 1
    final = 1 + x + conta
    return final
print(calcula_euler(2,2))