from math import radians
from math import cos
def calcula_trabalho(F,teta,s):
    trab = F*(radians(cos(teta)))*s
    return trab 

