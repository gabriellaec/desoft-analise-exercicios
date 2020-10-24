import math 
a=int(input("coloque a velocidade:"))
b=int(input("coloque o angulo:"))
d=a**2*math.sin(2*(math.pi*b/180))/9.8
if d<2:
    print("Acertou!")
elif d>2 and d<10:
    print("Muito perto")
else:
    print("Muito Longe")
    

