import math
velocidade= float(input("qual a velocidade?"))
angulo= float(input("qual o angulo de lançamento?"))
g= 9.8
d= ((velocidade**2)*math.sin(2*angulo))/g
if 98 < d < 102:
    print("Acertou!")
elif 90 < d < 105:
    print ("Muito perto")
else:
    print ("Muito longe")