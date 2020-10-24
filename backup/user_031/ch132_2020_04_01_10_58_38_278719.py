import math
def calcula_trabalho (forca, deslocamento, graus):
    grau= math.radians(graus)
    t= forca * deslocamento * math.cos(grau)
    print("O trabalho vale {} Joules" .format(t))
    