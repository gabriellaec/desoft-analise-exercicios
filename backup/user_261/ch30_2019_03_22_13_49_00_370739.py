import math 
a=float(input("coloque a velocidade:"))
b=float(input("coloque o angulo:"))
d=a**2*math.sin(math.radians(2*b))/9.8
if d>=98 and d<=102:
    print("Acertou!")
elif d<98:
    print("Muito perto")
else:
    print("Muito Longe")
    

