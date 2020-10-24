import math
g = 9.8
def jaca_math(v,ang):
    angc = ang * 2
    d = ((v ** 2) * math.sin(angc)) / g
    if d > 102:
        print("Muito longe")
    elif d < 102:
        print("Muito perto")
    else:
        print("Acertou!")
