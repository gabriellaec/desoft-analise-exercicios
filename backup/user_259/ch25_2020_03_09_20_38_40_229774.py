import math
v = float(input("Velocidade: "))
t = float(input("Angulo: "))
def bullseye(v,t):
    d=((v**2)*math.sin(math.radians(2*t)))/9.8
    if (d-100)<(-2):
        return "Muito perto"
    elif (abs(d-100))<2:
        return "Acertou!"
    else:
        return "Muito longe"
print(bullseye(v,t))
