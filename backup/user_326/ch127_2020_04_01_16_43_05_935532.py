import math

def calcula_enlogacao(amplitude, fase_inicial, velocidade_angular, segundos):
    coseno_fase_velocidade_tempo = math.cos(math.radians(fase_inicial) + math.radians(velocidade_angular) * segundos )
    enlongação_particula = amplitude * coseno_fase_velocidade_tempo 
    return enlongação_particula