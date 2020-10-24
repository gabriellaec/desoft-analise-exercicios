import math
from random import randint

#questão1

def snell_descartes (n1,n2,teta1):
    teta1r = math.radians(teta1)
    teta2r = math.asin((n1/n2)*math.sin(teta1r))
    teta2 = math.degrees(teta2r)
    return teta2  
    
