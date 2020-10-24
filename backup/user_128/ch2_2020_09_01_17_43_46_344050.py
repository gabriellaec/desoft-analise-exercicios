def checa_zero(variavel):
    if variavel == 0:
        print("Você nem saiu do lugar?")
        print("Pare de ser bobo e faça de novo")
        calcula_velocidade_media()

    else:
        pass

def calcula_velocidade_media():
    distancia = input("Quantos kilômetros você percorreu?")
    distancia = int(distancia)
    checa_zero(distancia)

    tempo = input("Quanto horas durou a sua viagem?")
    tempo = int(tempo)
    checa_zero(tempo)

    velocidade_media = distancia / tempo


    print("A sua velocidade média foi de {0}km/h".format(velocidade_media))

calcula_velocidade_media()