import math
v = input("Qual sua velocidade desejada?: ")
teta = input("Qual seu ângulo desejado?: ")
#teta = ang * 0.0174533
g = 9.8

d = ((v**2) * (math.sin(2*teta)))/g

if 98<=d<=102:
    print("Acertou!")
elif d<98:
    print("Muito perto")
elif d>102:
    print("Muito longe")