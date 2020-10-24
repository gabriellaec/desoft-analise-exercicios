import math

def distanciaJaca (v, a):
    a = math.radians(a)

    d = (((v**2)*math.sin(2*a))/9.8)


    if(d<98):
        return("Muito perto")
    elif(d>102):
        return("Muito longe")
    elif(d>=98) or (d<=102):
        return("Acertou!")

print(distanciaJaca(35, 27))