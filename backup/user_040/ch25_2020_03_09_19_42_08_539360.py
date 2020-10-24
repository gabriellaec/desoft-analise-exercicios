import math
v=float(input("Velocidade de lançamento: "))
angulo=float(input("Ângulo de lançamento: "))
def d(v,angulo):
    return (v**2*math.sin(math.radians(2*angulo))/9.8)
if (d>=102):
    print ("Acertou!")
elif (d<=98):
    print ("Muito perto")
else:
    print ("Muito longe")