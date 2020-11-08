import math

def calcula_gaussiana(x, mi, sigma):
    resposta =  1 / (sigma * math.pi) * exp(-0.5 * (((x - mi) / sigma)) ** 2
    return resposta