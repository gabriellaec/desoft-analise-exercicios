import math
v = float(input('Qual a velocidade? '))
teta= int(input('Qual ângulo? '))
d=(math.sin(2*teta*math.pi/180)*v**2)/9.8
if d>=98 and d<=102:
    print("Acertou!")
elif d<98:
    print ("Muito perto")
else :
    print ("Muito longe")