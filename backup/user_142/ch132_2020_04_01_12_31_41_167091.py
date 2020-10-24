from math import radians
from math import cos
def calcula_trabalho (F, Ang, S):
   
    Ang_radianos = radians(Ang)
    T = F*cos(Ang_radianos)*S
    
    return T
