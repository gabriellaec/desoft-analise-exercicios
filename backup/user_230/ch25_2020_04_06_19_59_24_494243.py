import math
v=float(input("Qual a velocidade de lançamento da jaca?"))
teta=float(input("Qual o ângulo de lançamento da jaca?"))
g=9.8
distancia=(v**2*math.sin(radians(2*teta)))/g    
if distancia<102 and distancia>98:
    print("Acertou!")
elif distancia<98:
    print("Muito perto")
elif distancia>102:
    print("Muito longe")