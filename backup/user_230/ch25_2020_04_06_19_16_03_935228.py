import math
v=int(input("Qual a velocidade de lançamento da jaca?"))
teta=float(input("Qual o ângulo de lançamento da jaca?"))
g=9.8
distancia=(v**2*math.sin(2*teta))/g    
if distancia==100 or distancia==99 or distancia==101:
    print("Acertou!")
elif distancia<99:
    print("Muito perto")
else:
    print("Muito longe")