import math
def calcula_trabalho (forca, deslocamento, graus):
    t= forca * deslocamento * math.cos(math.degrees(graus))
    print("O trabalho vale {} Joules" .format(t))