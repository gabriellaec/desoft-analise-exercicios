import math
def calcula_euler(x, n):
    soma_euler=0
    for i in range(n):
        euler = x**i/ math.factorial(i)
        soma_euler+=euler
    print(soma_euler)