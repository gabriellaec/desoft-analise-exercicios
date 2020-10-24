import math
def area_pentagono(l):
    a = (l/2) / math.tan(math.radians(54))
    A = 5 * l * a/2
    return A