import math

velocidade = float(input('Digite a velocidade de lançamento: '))
θ = float(input('Diite o ângulo de lançamento: '))
distancia = (velocidade**2*math.sin(2*math.radians(θ)))/9.8

if distancia < 98:
    print("Muito perto")
elif distancia > 102:
    print("Muito longe")
else:
    print("Acertou!")