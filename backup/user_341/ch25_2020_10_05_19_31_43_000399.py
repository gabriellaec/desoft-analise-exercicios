import math
def jacawars(v, t):
    distancia = (v**2*math.sin(2*math.radians(t))/ 9.8)
    if distancia >= 98 and distancia <= 102:
        return "Acertou"
    elif distancia > 102:
        return "Muito Longe"
    else:
        return "Muito perto"

v = float(input("Velocidade"))
t = float(input("Angulo"))
print(jacawars(v, t))

