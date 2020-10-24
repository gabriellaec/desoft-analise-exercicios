ang=float(input("insira o angulo de lançamento: "))
vel=float(input("insira a velocidade inicial do lançamento: "))
def distancia(ang,vel):
    import math
    dist=((vel**2)*math.sin(2*ang))/9.8
    return dist

if 98<=distancia(ang,vel)<=102:
    print("Acertou!")

elif distancia(ang,vel)>102:
    print("Muito longe")
else:
    print("Muito perto")


