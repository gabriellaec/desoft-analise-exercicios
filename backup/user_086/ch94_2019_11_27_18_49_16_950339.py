vmax = int(input('Qual é a velocidade máxima da via (em km/h)? '))
vmax = vmax/3.6 #em m/s
dcam = int(input('Qual a distância entre as duas câmeras (em metros)? '))

placas = {}
loop = True
while loop:
    placa = input('Qual é a placa do carro? ')
    if not placa in placas:
        placas.append(placa)
        tinicial = int(input('Qual é o tempo marcado?'))
    else:
        tfinal = int(input('Qual é o tempo marcado?'))
    vplaca = distancia/(tfinal- tinicial)
    if vplaca>vmax and vplaca<=vmax*1.2:
        print('A infração é média e a penalidade é multa de R$ 130,16')
    if vplaca>vplaca*1.2 and vplaca<= vplaca*1.5:
        print('A infração é grave e a penalidade é multa de R$ 195,23')
    if vplaca>vplaca*1.5:
        multa = 3*195,23
        print('A infração é gravíssima e a penalidade é multa de {0} e a suspenção imediata da sua carteira de motorista'.format(multa))