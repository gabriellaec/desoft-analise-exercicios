import math
def calcula_trabalho (forca, deslocamento, graus):
    grau= math.radians(graus)
    t= forca * math.cos(grau) * deslocamento
    