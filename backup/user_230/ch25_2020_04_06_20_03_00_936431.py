from math import sin,radians
v=float(input("Qual a velocidade de lançamento da jaca?"))
teta=float(input("Qual o ângulo de lançamento da jaca?"))
g=9.8
distancia=(v**2*sin(radians(2*teta)))/g    
if distancia>102:
    print("Muito longe")
elif distancia<=98:
    print("Muito perto")
else:
    print("Acertou!")