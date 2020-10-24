import math
def calcula_euler(x, n):
    resposta = 0
    for i in range(n):
        resposta += (x**n)/(math.factorial(n))
    return resposta