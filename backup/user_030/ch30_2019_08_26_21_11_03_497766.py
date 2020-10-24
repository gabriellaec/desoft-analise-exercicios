import math
v = int(input("velocidade: "))
t = int(input("angulo: "))
def jaca_wars(v, t):
    d = ((v**2)*math.sin(2*t))/9.8
    if d <= 102 and d >= 98:
        return "Acertou"
    elif d > 102:
        return "muito longe"
    else d < 98:
        return "muito perto"
print(jaca_wars(v, t))
