import math
def jacawars(v, t):
    distancia = (v**2*math.sin(2*t)/ 9.8)
    if distancia >= 98 and <= 102:
        return "Acertou"
    elif distancia > 102:
        return "Muito Longe"
    else:
        return "Muito Perto!"
    