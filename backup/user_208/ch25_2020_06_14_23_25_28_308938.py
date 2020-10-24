import math
v = float(input("Qual a velocidade do lançamento? "))
a = float(input("Qual o ângulo de lançamento? "))
g = 9.8
angulo = math.radians(a)
d= ((v**2)*math.sin(angulo))/g

if  d <= 102 and d >= 98:
    print ("Acertou!")
elif d <= 97:
    print ("Muito perto")
elif d >= 103:
    print ("Muito longe")
   
   