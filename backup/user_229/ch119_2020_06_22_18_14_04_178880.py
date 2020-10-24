import math
def calcula_euler(x, n):
    resposta = 0
    for i in range(n):
        resposta += (x**i)/(math.factorial(i))
    return resposta