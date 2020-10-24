import math
def calcula_trabalho (forca, deslocamento, graus):
    t= forca * deslocamento * math.degrees.cos(graus)
    print("O trabalho vale {} Joules" .format(t))