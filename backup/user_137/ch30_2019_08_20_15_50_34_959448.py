import math

v = int(input("Digite a velocidade da sua jaca! "))
o = int(input("Digite seu ângulo de arremesso de jaca! "))
o = math.sin(2 * math.radians(o))
g = 9.8

d = (v ** 2 / g) * o

if d >= 98 and d <= 102:
    print("Acertou!")
elif d <= 98 and d >= 90 or d >= 102 and d <= 110:
    print("Muito perto")
else:
    print("Muito longe")