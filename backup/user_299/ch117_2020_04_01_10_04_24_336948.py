import math
from random import randint

#questão1

def snell_descartes (n1,n2,teta1):
    teta2_rad = math.asin(math.sin(teta1*math.pi/180)*n1/n2)
    teta2 = teta2_rad*math.pi/180
    return teta2 
