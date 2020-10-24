dist=float(input("Distancia percorrida:"))
tempo=float(input("Tempo gasto:"))

def calcula_velocidade_media(dist,tempo):
    y=dist/tempo
    return y

print(calcula_velocidade_media(dist,tempo))