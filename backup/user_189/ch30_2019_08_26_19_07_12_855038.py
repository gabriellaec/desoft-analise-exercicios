def distancia(ang,vel):
    import math
    dist=((vel**2)*math.sin(2*ang))/9.8
    return dist

if 98<=dist<=102:
    print("Acertou!")

elif dist>102:
    print("Muito longe")
else:
    print("Muito perto")


