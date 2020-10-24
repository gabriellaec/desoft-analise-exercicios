import math
v = float(input('Qual a velocidade? '))
teta= float(input('Qual ângulo? '))
d=(math.sin(2*teta)*v**2)/9.8
if d>98 and d<102:
    print("Acertou!")
elif d<98 and d>102:
    print ("Muito perto")
else :
    print ("Muito longe")