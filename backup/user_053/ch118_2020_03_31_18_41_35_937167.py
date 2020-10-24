import math


def reflexao_total_interna(n1, n2, angulo_2_grau):
    seno_angulo_1 = (n2/n1)*math.sin((angulo_2_grau*math.pi)/180)
    reflexao_total = True 
    if seno_angulo_1 > 1:
        reflexao_total = True
    else:
        reflexao_total = False
    return reflexao_total

print(reflexao_total_interna(1, 1.3, 30))