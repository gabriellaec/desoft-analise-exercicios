from math import radians
from math import cos
def calcula_trabalho (F, A, S):
   
    A_radianos = radians(A)
    T = F*A_radianos*S
    
    return T
