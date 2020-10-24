import math
v = int(input("Qual a velocidade do lançamento? "))
a = int(input("Qual o ângulo de lançamento? "))
g = 9.8
d= ((v**2)*math.rad(2*a))/g
if  d <= 102 and d >= 98:
    print ("Acertou!")
elif d <= 97:
    print ("Muito perto")
elif d >= 103:
    print ("Muito longe")
   
   