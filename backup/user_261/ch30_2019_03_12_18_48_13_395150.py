import math 
a=int(input("coloque a velocidade:"))
b=int(input("coloque o angulo:"))
d=a**2*math.sin(math.radians(2*b))/9.8
if d<2:
    print("Acertou!")
elif d>2 and d<=10:
    print("Muito perto")
else:
    print("Muito Longe")
    

