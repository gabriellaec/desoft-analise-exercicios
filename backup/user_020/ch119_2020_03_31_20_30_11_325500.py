import math
def calcula_euler(x,n):
    cont = 0
    euler = []
    while cont<n:
        y = x**cont/math.factorial(cont)
        euler.append(y)
        cont+=1
        print(euler)
    soma_euler = sum(euler)
    print (soma_euler)
    return soma_euler