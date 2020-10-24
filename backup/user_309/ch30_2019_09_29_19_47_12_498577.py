import math
vel = float(input("Digite a velocidade: "))
ang = float(input("Digite o angulo de lancamento: "))
raio = 2
g = 9.8
distancia = ((vel**2)*(math.sin(2*ang)))/g
if distancia < raio:
    print("Muito Perto")
elif distancia > raio:
    print("Muito longe")
else:
    print("Acertou!")