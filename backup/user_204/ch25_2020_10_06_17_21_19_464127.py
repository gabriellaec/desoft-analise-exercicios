import math
g = 9.8
def catapulta(v,ang):
    ang_graus = 2 * ang
    d = ((v ** 2) * math.sin(math.radians(ang_graus))) / g 
    if d <= 102 or d >= 98:
        return "Acertou!"
    elif d < 98:
        return "Muito perto"
    else:
        return "Muito longe"