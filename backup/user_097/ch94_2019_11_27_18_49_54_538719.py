velocidade_maxima = int(input("Informe a velocidade máxima da via em Km/h: "))

distancia_cameras = int(input("Informe a distancia entre as câmeras em m: "))

placas = []
tempos = []

placas.append(input("Informe a placa do veículo: "))
tempos.append(int(input("Informe o instante em que o veículo passou: ")))

while True != "":

    placa = input("Informe a placa do veículo: ")

    if (placa == ""):
        break

    tempo = int(input("Informe o instante em que o veículo passou: "))
    tempos.append(tempo)