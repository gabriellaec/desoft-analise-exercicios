from math import asin, sin, pi

def snell_descartes(indice_1, indice_2, angulo_incidente):
    ''' calcula o ângulo de refração de um raio de luz
        a partir dos índices de refração dos meios e do
        ângulo de incidência '''
    
    angulo_incidente *= pi / 180
    seno_incidente = sin(angulo_incidente)
    seno_refracao = indice_1 / indice_2 * seno_incidente
    angulo_refracao = asin(seno_refracao) * 180 / pi
    
    return angulo_refracao
    
    