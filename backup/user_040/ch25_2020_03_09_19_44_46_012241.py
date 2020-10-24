import math
v=float(input("Velocidade de lançamento: "))
angulo=float(input("Ângulo de lançamento: "))
def d(v,angulo):
    d = (v**2*math.sin(math.radians(2*angulo))/9.8)
    if (d>=102):
        return ("Acertou!")
    elif (d<=98):
        return ("Muito perto")
    else:
        return ("Muito longe")