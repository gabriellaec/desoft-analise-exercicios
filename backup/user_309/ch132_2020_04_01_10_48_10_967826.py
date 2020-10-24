from math import radians
from math import cos
def calcula_trabalho(F,teta,s):
    teta_em_rad = radians(teta)
    trab = F*cos(teta_em_rad)*s
    return trab 

