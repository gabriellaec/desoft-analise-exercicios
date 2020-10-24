import math

def area_pentagono(l):
    angulo = math.radians(54)
    a = (l/2) * math.tan(angulo)

    area = ((a * l) / 2) * 5
    return area