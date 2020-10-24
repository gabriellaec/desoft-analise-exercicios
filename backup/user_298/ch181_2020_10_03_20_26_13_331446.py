import math
def area_pentagono(l):
    ang = math.radians(36)
    a = (l/2)/math.tan(ang)
    area_t = (l*a)/2
    area_total = area_t*5
    return area_total