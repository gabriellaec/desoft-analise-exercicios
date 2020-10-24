from math import sqrt

def distancia_euclidiana(x1, y1, x2, y2):
    
    delta_x = x1 - x2
    delta_y = y1 - y2
    
    return sqrt(delta_x ** 2 + delta_y ** 2)