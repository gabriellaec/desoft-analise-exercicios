import math
def calcula_pi(n):
    n = range(1,n+1)
    c = 0
    resposta = 0
    for i in n:
        c = 6/(i**2)
        resposta += c
    resposta = math.sqrt(resposta)
    return resposta 