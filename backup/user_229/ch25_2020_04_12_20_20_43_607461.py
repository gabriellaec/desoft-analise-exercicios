import math
g=9.8
def jaca(v,T):
    d=(v**2)*(math.sin(2*math.radians(T)))/g
    if 98 <= d and d <= 102:
        return "Acertou!"
    elif d < 98:
        return "Muito perto"
    else:
        return "Muito longe"