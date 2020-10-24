import math

v=float(input("EScolha a velocidade:"))
a= float(input("Escolha o ângulo:"))

d= ((v**2)*(math.sin(2*a)))/9.8

if 98 < d < 100 or 100 < d < 102 or d==100:
    print("Acertou!")
if 97< d < 98 or 102 < d < 103:
    print("Muito perto")
else: 
    print("Muito longe")