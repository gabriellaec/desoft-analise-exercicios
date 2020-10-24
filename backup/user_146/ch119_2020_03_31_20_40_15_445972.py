import math
def calcula_euler(x,n):
    expo = 0
    euler = []
    while expo<n:
        y = x**expo/math.factorial(expo)
        euler.append(y)
        expo+=1
        print(euler)
    soma_euler = sum(euler)
    return soma_euler
