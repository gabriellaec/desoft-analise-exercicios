import math
a=float(input("velocidade:"))
b=float(input("ângulo:"))
g=9.8
d=a**2*(math.sin(2*b*math.pi/180))/g
if d>=98 and d<=102: 
    print ("Acertou!")
elif d<98:
    print ("Muito perto")
else:
    print("Muito longe")
