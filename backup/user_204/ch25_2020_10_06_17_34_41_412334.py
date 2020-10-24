import math
g = 9.8
v = float(input("velocidade: "))
ang = float(input("angulo: "))
def catapulta(v,ang):
    ang_graus = 2 * ang
    d = ((v ** 2) * math.sin(math.radians(ang_graus))) / g 
    if d <= 102 and d >= 98:
        return "Acertou!"
    elif d < 98:
        return "Muito perto"
    else:
        return "Muito longe"