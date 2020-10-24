import math

def calcula_trabalho (F, teta, s):
    
    teta = math.radians(teta)
    
    return(F*math.cos(teta)*s)