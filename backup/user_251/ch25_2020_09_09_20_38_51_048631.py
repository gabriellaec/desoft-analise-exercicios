import math
def distancia_jaca(v,o):
    d = ((v**2)*(math.sin(2*(o/180)*math.pi)))/9.8
    if d > 98 and d < 102:
        return "Acertou!"
    else:
        if d <= 98 and d >= 50 or d >= 102 and d <= 150:
            return "Muito perto"
        else:
            if d < 50 or d > 150:
                return "Muito longe"

v = float(input("Diga a velocidade da jaca: "))
o = float(input("Diga o angulo da catapulta: "))

print(distancia_jaca(v,o))



