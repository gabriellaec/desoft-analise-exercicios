import math
g=9.8
def jaca(v,T,g):
    d=(v**2)*math.sin(2*T)/g
    if 98 <= d <= 100:
        return "Acertou!"
    elif d < 98:
        return "Muito perto"
    else:
        return "Muito longe"