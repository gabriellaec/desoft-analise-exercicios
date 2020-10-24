import math
vel = float(input("qual a velocidade da sua jaca, juca?"))
ang = float(input("qual o ângulo de lançamento?"))
d = (vel**2*math.sin(2*ang)/9.8) +2
if 98<=d and d<=102:
    print ("Acertou!")
elif d<98:
    print ("Muito perto")
else: 
    print ("Muito longe")