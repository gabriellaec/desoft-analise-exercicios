import math

v=int(input("Digite a velocidade"))
an=int(input("Digite o angulo"))

distancia=((v**2)*math.sin(2*an))/9.8

if distancia<=96:
    print("Muito perto")
elif distancia>=104:
    print("Muito longe")
else:
    print("Acertou!")