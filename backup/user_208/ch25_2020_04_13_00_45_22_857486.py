import math
v = int(input("Qual a velocidade do lançamento? "))
a = int(input("Qual o ângulo de lançamento? "))
g = 9.8
seno = math.sin(2*a)
graus = math.degrees (seno)
d= ((v**2)*graus)/g
if  d <= 102 and d >= 98:
    print ("Acertou!")
elif d <= 97:
    print ("Muito perto")
elif d >= 103:
    print ("Muito longe")
   
   