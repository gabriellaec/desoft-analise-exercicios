import math

def distancia_euclidiana (x1, y1, x2, y2):
    delta_x = math.abs(x1 - x1)
    delta_y = math.abs(y2 - y1)
    
    distance = math.sqrt(delta_x**2 + delta_y**2)
    
    return distance
    