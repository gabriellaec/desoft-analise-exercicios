import math
def jacawars(v, t):
    distancia = (int(v**2*math.sin(2*t)/ 9.8))
    if distancia == 100:
        return "Acertou"
    elif distancia > 100:
        return "Muito Longe"
    else:
        return "Muito Perto!"
    