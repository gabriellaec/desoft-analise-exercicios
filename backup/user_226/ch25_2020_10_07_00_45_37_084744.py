import math

velocidade = int(input("Qual a velocidade? "))
angulo = int(input("Qual a angulo? "))
angulo = math.radians(angulo)

def calcula_distancia(v, a):
    distancia = v ** 2 * math.sin(2 * a) / 9.8
    return distancia

def mede_acerto(distancia):
    if distancia < 98:
        return "Muito perto"
    elif 98 <= distancia <= 102:
        return "Acertou!"
    elif distancia > 102:
        return "Muito Longe"

distancia = calcula_distancia(velocidade, angulo)
mede_acerto(distancia)

