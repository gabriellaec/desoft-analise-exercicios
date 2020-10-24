from math import cos, radians

def calcula_trabalho(forca, angulo, deslocamento):
    
    angulo = radians(angulo)
    cosangulo = cos(angulo)
    
    return cosangulo * forca * deslocamento