import math
g = 9.8
def jaca_math(v,ang):
    d = ((v ** 2) * math.sin(2 * ang)) / g
    return d
    if d > 102:
        print("Muito longe")
    elif d < 102:
        print("Muito perto")
    else:
        print(Acertou!)
