vel_max = int(input("Qual a velocidade máxima da via, em km/h?"))
d = float(input("Qual a distância entre as câmeras, em metros?"))

vel_max = vel_max/3.6
veiculos = {}
placa = input("Qual a placa do veículo?")
while placa != '':
    tempo = float(input("Em qual instante?"))
    if placa in veiculos:
        delta_t = tempo - veiculos[placa]
        velocidade = d/delta_t
        if velocidade <= vel_max:
            print("O veículo está dentro do limite de velocidade")
        elif velocidade > vel_max and velocidade <= 1.2*vel_max:
            print('O veículo cometeu infração média, com multa de R$ 130,16.')
        elif velocidade > 1.2*vel_max and velocidade <= 1.5*vel_max:
            print('O veículo cometeu infração grave, com multa de R$ 195,23.')
        else:
            print('O veículo cometeu infração gravíssima, com multa 3x de R$ 195,23, suspensão imediata do direito de dirigir e apreensão do documento de habilitação')
        del veiculos[placa]
    else:
        veiculos[placa] = tempo
        print('O veículo está passando pela primeira câmera.')
    placa = input("Qual a placa do veículo?")