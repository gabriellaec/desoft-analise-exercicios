import math
velocidade=int(input("Digite a velocidade: "))
angulo=int(input("Digite o ângulo: "))
d=(velocidade**2*math.sin(2*math.degrees(angulo)))/9.8
if d<98:
    print ("Muito perto")
elif d>102:
    print ("Muito longe")
else:
    print ("Acertou!")