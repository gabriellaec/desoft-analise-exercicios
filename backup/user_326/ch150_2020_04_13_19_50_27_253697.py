from math import sqrt
def calcula_pi(numero_de_termos):
    indice = 1
    aproximacao_pi_ao_quadrado = 0
    while indice < numero_de_termos:
        aproximacao_pi_ao_quadrado += 6 / indice ** 2
        indice += 1
    aproximacao_pi = sqrt(aproximacao_pi_ao_quadrado)
    return aproximacao_pi