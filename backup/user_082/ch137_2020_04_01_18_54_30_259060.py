import math
def calcula_aceleracao(raio, frequencia_rpm):
    frequencia_hz= frequencia_rpm / 60
    velocidade_angular= 2* math.pi * frequencia_hz
    ac= ((velocidade_angular) ** 2) * raio
    return ac