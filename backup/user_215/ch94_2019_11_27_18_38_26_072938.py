vel_max = int(input("Qual a velocidade máxima da via (em km/h)? "))
distancia = int(input("Qual a distancia entre as cameras (em metros)? "))
carros = {}

while True:
    placa = str(input("Insira a placa do veiculo: "))
    if len(placa) != 7:
        print("Erro, insira uma placa valida! ")
        break
    if len(placa) == 0:
        break
    instante = int(input("Insira o instante (em segundos) que o carro foi visualizado pela camera: "))
    if placa not in carros:
        carros[placa] = instante
    else:
        vel_real = (distancia / (instante - carros.get(placa))) / 0.6
        if vel_max < vel_real:
            if vel_real < vel_max * 1.2:
                print("O carro foi multado em R$130,16 , por superar a velocidade maxima em ate 20%, esta é uma infracao media")
            elif vel_max * 1.5 > vel_real > vel_max * 1.2:
                print("O carro foi multado em R$195,23 , por superar a velocidade maxima em mais de 20%, sem ultrapassar os 50%, esta é uma infracao grave")
            elif vel_real > vel_max * 1.5:
                print("O carro foi multado em 3 x R$195,23, por superar a velocidade maxima em mais de 50%, esta é uma infracao gravissima e o motorista está suspenso do direito de dirigir")
        else:
            del carros[placa]


