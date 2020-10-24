import math
v = int(input("Qual sua velocidade desejada?: "))
ang = int(input("Qual seu ângulo desejado?: "))
teta = ang * (math.pi/180)
g = 9.8

d = ((v**2) * (math.sin(2*teta)))/g

if 98<=d<=102:
    print("Acertou!")
elif d<98:
    print("Muito perto")
elif d>102:
    print("Muito longe")