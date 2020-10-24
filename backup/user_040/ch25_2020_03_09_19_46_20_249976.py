from math import sin,radians
g=9.8
v=float(input("Velocidade de lançamento: "))
angulo=float(input("Ângulo de lançamento: "))
def d(v,angulo):
    d = (v**2*sin(radians(2*angulo))/g)
    if (d>=102):
        return ("Acertou!")
    elif (d<=98):
        return ("Muito perto")
    else:
        return ("Muito longe")
print (d)