from math import radians
from math import cos
def calcula_trabalho (F, theta, s):
   
    theta_radianos = radians(theta)
    T = F*theta_radianos*s
    
    return T
