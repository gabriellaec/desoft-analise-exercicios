import math

v= float(input("Insira velocidade (em m/s): \n"))
a= float(input("Insira angulo (em graus): \n"))

g=9.8

#Transformando graus em radianos

a=(math.pi*a)/180

d=(v**2*math.sin(2*a))/g

if(d>98) and (d<100):
    print("Acertou")
elif (d<=98):
    print("Muito perto")
else:
    print("Muito longe")

    