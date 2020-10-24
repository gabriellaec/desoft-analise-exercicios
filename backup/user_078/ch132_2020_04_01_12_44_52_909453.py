import math
def calcula_trabalho (F, O, S):
    t = F * math.degrees(math.cos(math.radians(O))) * S
    return t