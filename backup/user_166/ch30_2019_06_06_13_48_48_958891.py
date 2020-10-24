import math
velocidade= int(input("qual a velocidade?"))
angulo= int(input("qual o angulo de lançamento?"))
g= 9.8
d= ((velocidade**2)*sin(2*angulo))/g
if 98 < d < 102:
    print("Acertou!")
elif 90 < d < 105:
    print ("Muito perto")
else:
    print ("Muito longe")