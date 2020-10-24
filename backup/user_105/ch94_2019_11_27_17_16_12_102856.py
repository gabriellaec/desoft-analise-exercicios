vel_da_via = int(input('Qual a velocidade maxima nessa via em km/h? '))
dist_entre_cameras = int(input('Qual a distancia entre as 2 cameras em metros? '))
placa = '0000000'
while len(placa) != 0:
    placa = input('Qual a placa do veiculo? ')
    if len(placa)==0:
        break
    

    cam1 = float(input('quando o carro passou pelo radar 1? '))
    cam2 = float(input('Quando o carro passou pelo radar 2? '))
    tempo = abs(cam1-cam2)
    vel_carro = (dist_entre_cameras/tempo)*3.6
    if vel_carro+vel_carro*0.5 > vel_da_via:
        print('Carro com a placa {0} passou da velocidade permitida nessa via, sua infração é gravissima e a multa a ser paga é de 585.69 reais'.format(placa))
    elif vel_carro+vel_carro*0.2 > vel_da_via and vel_carro+vel_carro*0.5 < vel_da_via:
        print('Carro com a placa {0} passou da velocidade permitida nessa via, sua infração é grave e a multa a ser paga é de 195.23 reais'.format(placa))
    elif vel_carro+vel_carro*0.2 > vel_da_via:
        print('Carro com a placa {0} passou da velocidade permitida nessa via, sua infração é meédia e a multa a ser paga é de 130.16 reais'.format(placa))
    else:
        print('Carro com a placa {0} esta de boa'.format(placa))   