import math
from random import randint


def reflexao_total_interna (n1,n2,teta2):
    ang_limite_rad = math.asin(n1/n2)
    ang_limite = math.degrees(ang_limite_rad)
    teta2r  math.radians(teta2)
    teta1r = math.asin(math.sin(teta2r)*(n1/n2))
    teta1 = math.degrees(teta1r)
    if ang_limite<=teta2 and n2>n1:
        return True
    else:
        return False