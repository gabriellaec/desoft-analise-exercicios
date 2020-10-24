import math


gravity = 9.8

def calcula_distancia_do_projetil (speed, phi, height):
    energy = speed**2 / gravity / 2
    sin_phi_squared = math.sin(phi)**2
    sin_2phi = math.sin(phi * 2)
    crazy = math.sqrt(gravity * height / speed**2 / sin_phi_squared * 2 + 1) + 1
    
    distance = energy * crazy * sin_2phi
    return distance
