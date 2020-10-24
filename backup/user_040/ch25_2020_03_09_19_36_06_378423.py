import math
v=float(input("Velocidade de lançamento: "))
angulo=float(input("Ângulo de lançamento: "))
if (-2<(v**2*math.sin(2*angulo)/9.8)-100<2):
    print ("Acertou!")
elif ((v**2*math.sin(2*angulo)/9.8)-100<-2):
    print ("Muito perto")
else:
    print ("Muito longe")