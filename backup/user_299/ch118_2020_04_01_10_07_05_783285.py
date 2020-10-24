import math
from random import randint


def reflexao_total_interna (n1,n2,teta2):
    ang_limite_rad = math.asin(n1/n2)
    ang_limite = ang_limite_rad*math.pi/180
    teta1_rad = math.asin(math.sin(teta2*math.pi/180)*n1/n2)
    teta1 = teta1_rad*math.pi/180
    if ang_limite<teta1:
        return True
    else:
        return False
