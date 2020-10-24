from math import radians
from math import cos
def calcula_trabalho (F, A, S):
   
    A_radianos = radians(A)
    T = F*cos(A_radianos)*S
    
    return T
