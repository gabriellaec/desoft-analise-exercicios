import math 
a=int(input("coloque a velocidade:"))
b=int(input("coloque o angulo:"))
d=a**2*math.sin(math.radians(2*b))/9.8
if d<98:
    print("Acertou!")
elif d>102 and d<100:
    print("Muito perto")
else:
    print("Muito Longe")
    

