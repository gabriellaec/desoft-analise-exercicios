import math
v = float(input("Qual a velocidade"))
o = math.radians(float(input("Qual o ângulo")))
d = ((v**2)*math.sin(2*o))/9.8
if d < 98:
    print ("Muito perto")
if d > 102:
    print("Muito longe")
else:
    print("Acertou!")