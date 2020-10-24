from math import sqrt
def distancia_euclidiana(a,b,c,d):
    delta_x2 = ((c - a)**2)
    delta_y2 = ((d - b)**2)
    dist = sqrt(delta_x2 + delta_y2)
    return dist