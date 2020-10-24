import math
g = float(9.8)
v = int(input("diga a velocidade da jaca: "))
graus = int(input("diga o angulo de lançamento da jaca: "))
d = ((v**2) * math.sin(2*graus))/g
if d >= 98 and d <= 102:
    print("Acertou!")
elif d >= 102 and d <= 120:
    print("Muito perto")
else:
    print("Muito longe")
    