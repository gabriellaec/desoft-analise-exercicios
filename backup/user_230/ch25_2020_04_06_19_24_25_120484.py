import math
v=int(input("Qual a velocidade de lançamento da jaca?"))
teta=int(input("Qual o ângulo de lançamento da jaca?"))
g=9.8
distancia=(v**2*math.sin(2*teta))/g    
if distancia<102 and distancia>98:
    print("Acertou!")
elif distancia<98:
    print("Muito perto")
elif distancia>102:
    print("Muito longe")