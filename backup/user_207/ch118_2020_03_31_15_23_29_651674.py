from math import sin, asin, pi, sqrt
n1 = 1.0
n2 = 1.0
theta02 = 30 #valor em GRAUS


def reflexao_total_interna (n1,n2,theta02):
    seno_theta01 = n1/n2 * sin(theta02/360 *2*pi)  #aqui, retorna o valor numérico do SENO
    sen_Limite = n2/n1 * seno_theta01

    if seno_theta01 > sen_Limite:
        return True
    else:
        return False 