from math import tan, pi

tan_57 = tan(57 * pi / 180)

def area_pentagono(lado):
    
    altura_triangulo = tan_57 * lado / 2
    area_triangulo = altura_triangulo * lado / 2
    
    return 5 * area_triangulo
    
