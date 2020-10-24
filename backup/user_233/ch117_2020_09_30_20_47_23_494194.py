from math import asin, sin, pi

def snell_descartes(indice_1, indice_2, angulo_incidente):
    ''' retorna o ângulo de refração de um raio de luz
        em graus a partir dos índices de refração dos
        meios e do ângulo de incidência em graus '''
    
    # converte o ângulo de incidência para radianos
    angulo_incidente *= pi / 180
    
    # calcula o seno do ângulo de incidência
    seno_incidente = sin(angulo_incidente)
    
    # calcula o seno do ângulo de refração com base na lei de Snell-Descartes
    seno_refracao = indice_1 / indice_2 * seno_incidente
    
    # calcula o ângulo de refração a partir de seu seno e converte para graus
    angulo_refracao = asin(seno_refracao) * 180 / pi
    
    # retorna o valor do ângulo em graus
    return angulo_refracao
    
    