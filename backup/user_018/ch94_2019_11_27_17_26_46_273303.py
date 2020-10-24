#perguntas 
velocidade = float(input("Qual a velocidade máxima da via? "))
distancia = float(input("Qual a distância entre as duas câmeras? "))

velocidadev = 0

#loop
placa = 0
while placa != 'vazio':

    placa = input("Qual a placa do veículo? (para finalizar digite 'vazio') ")
    if placa == 'vazio':
        break 

    t1 = int(input("Em qual instante o veículo passou pela câmera 1?"))
    t2 = int(input("Em qual instante o veículo passou pela câmera 2?"))

    velocidadev = distancia*1000/(t2-t1) 
    print('Placa do veículo:', placa)
    print('Velocidade do veículo :', velocidadev)

    if velocidadev > velocidade and velocidadev <= velocidade*0.2:
        print("Infração média - Multa R$130,16")
    if velocidadev > velocidade*0.2 and velocidadev <= velocidade*0.5:
        print('Infração grave - multa R$195,23')
    if velocidadev > velocidade*0.5:
        print('Infração gravíssima - multa R$195,23 x 3 + suspensão imediata do direito de dirigir')