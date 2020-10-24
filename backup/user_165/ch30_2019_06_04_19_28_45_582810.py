import math
g = 9.8
raio_espalhamento = 2
velocidade = int(input("Valor da velocidade: "))
valor_angulo = int(input("Valor do angulo: "))
distancia = ((velocidade**2 *math.sin(2*valor_angulo))/g)
if distancia == 100:
    print("Acertou")
elif distancia > 100:
    print("Muito longe")
else:
    print("Muito perto")
