from math import sin,radians
v=float(input("Velocidade de lançamento: "))
angulo=float(input("Ângulo de lançamento: "))
g=9.8
def d(v,angulo):
    d = (v**2*sin(radians(2*angulo))/g)
    if (d>=102):
        return ("Acertou!")
    elif (d<=98):
        return ("Muito perto")
    else:
        return ("Muito longe")
print (d)