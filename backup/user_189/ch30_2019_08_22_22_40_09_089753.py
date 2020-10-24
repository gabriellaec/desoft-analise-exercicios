import math
def distancia(ang,vel):
    dist=((vel**2)*math.sin(2*ang))/9.8
    return dist

if 98<=distancia(ang,vel)<=102:
    print("Acertou!")

elif distancia(ang,vel)>102:
    print("Muito longe")
else:
    print("Muito perto")


