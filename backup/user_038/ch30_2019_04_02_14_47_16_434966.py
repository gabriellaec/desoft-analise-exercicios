import math
velo = float(input("Informe a velocidade de lançamento: "))
angulo = float(input("Informe o angulo de lançamento: "))
d = velo**2*math.sin(2*angulo)/9.8
if d>=102:
    print("Muito longe")
elif d<=98:
    print("Muito perto")
else:
    print("Acertou")