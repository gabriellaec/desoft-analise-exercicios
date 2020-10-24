import math
vel = int(input("qual a velocidade da sua jaca, juca?"))
ang = int(input("qual o ângulo de lançamento?"))
d = (vel**2*math.sin(2*ang*math.pi/180)/9.8) 
if 98<d or d<102:
    print ('Acertou!')
elif d<=98:
    print ('Muito perto')
else: 
    print ('Muito longe')