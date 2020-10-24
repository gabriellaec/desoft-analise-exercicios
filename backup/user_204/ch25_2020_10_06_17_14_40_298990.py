import math
g = 9.8
def catapulta(v,ang):
    ang_graus = math.radians(ang)
    d = ((v ** 2) * math.sin(2 * ang_graus)) / g 
    if d <= 102 or d >= 98:
        return "Acertou!"
    elif d > 102:
        return "Muito longe"
    else:
        return "Muito perto"