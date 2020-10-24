vel_max = float(input('Digite a velocidade max(km/h): '))
dist_cam = float(input('Digite a distancia entre as duas cameras(m):'))

placa = input('digite a placa do veiculo:')
while placa != '':    
    instante = int(input('digite o instante que o carro passou: '))
    velocidade = vel_max-(instante/dist_cam)
    if velocidade == 0.2*vel_max:
        print('Vc excedeu o limite de velocidade, sua multa eh de R$130,16')
    elif velocidade > 0.2*vel_max and velocidade <= 0.5*vel_max:
        print('Vc excedeu o limite de velocidade, sua multa eh de R$195,23' )
    elif velocidade > 0.5*vel_max:
        multa = 3*195.23
        print('Vc excedeu o limite de velocidade, sua multa eh de R${0:.2f}'.format(multa))
    else:
        placa = input('digite a placa do veiculo:')
        instante = int(input('digite o instante que o carro passou: '))