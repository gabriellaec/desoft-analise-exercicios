from math import cos
from math import radians

def calcula_trabalho (F, Ang, S):
   
    Ang_radianos = radians(Ang)
    T = F*cos(Ang_radianos)*S
    
    return T
