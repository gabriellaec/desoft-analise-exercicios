from math import sin, asin, pi, sqrt
n1 = 1.0
n2 = 1.0
theta02 = 30 #valor em GRAUS


def reflexao_total_interna (n1, n2, theta02):
    sen_theta01 = n2/n1 * sin(theta02/180 *pi)

    if sen_theta01 > 1:
        return True
    else:
        return False