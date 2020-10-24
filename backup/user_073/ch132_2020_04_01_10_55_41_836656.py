import math
def calcula_trabalho(F,theta,s):
    theta_em_rad=math.radians(theta)
    t= F*(theta_em_rad)*s
    return t