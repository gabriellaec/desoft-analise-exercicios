def calcula_velocidade_media():
    distancia = input("Quantos kilômetros você percorreu?")
    tempo = input("Quanto horas durou a sua viagem?")

    velocidade_media = distancia / tempo

    print("A sua velocidade média foi de {0}km/h".format(velocidade_media))