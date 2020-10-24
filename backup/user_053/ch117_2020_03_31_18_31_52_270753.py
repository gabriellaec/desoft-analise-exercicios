import math

def snell_descartes(n1, n2, angulo_1_grau):
    angulo_1_radiano = (angulo_1_grau*math.pi)/180
    seno_angulo_2 = (n1/n2)*math.sin(angulo_1_radiano)
    angulo_2_radiano = math.asin(seno_angulo_2)
    angulo_2_grau = (angulo_2_radiano*180)/math.pi

    return angulo_2_grau

alpha = snell_descartes(1.3, 2, 30)

print('O ângulo de refração é {0} graus'.format(alpha))