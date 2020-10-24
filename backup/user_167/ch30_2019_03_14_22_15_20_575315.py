import math
a=int(input("velocidade:"))
b=int(input("ângulo:"))
g=9.8
d=a**2*(math.sin(2*b*math.pi/180))/g
if d>=98: 
    print ("Muito perto")
else:
    print ("muito longe")
