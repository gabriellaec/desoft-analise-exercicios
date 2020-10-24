vel_max = float(input('Entre com a velocidade máxima em km/h:\n>>>> '))
d = float(input('Entre com a distância entre as câmeras em m:\n>>>> '))
placa = 'a'
dicionario = {}
while placa != '':
    placa = input('Entre com a placa do carro:\n>>>> ')
    if placa == '':
        break
    instante = float(input('Entre com o instante registrado:\n>>>> '))
    if placa not in dicionario:
        dicionario[placa] = instante
    else:
        delta_t = instante-dicionario[placa]
        vel = (d/delta_t)*3.6
        if vel <= vel_max:
            print('Tudo tranquilo...')
        elif vel > vel_max and vel <= 1.2*vel_max:
            print('INFRAÇÃO MÉDIA\nMULTA DE 130,16 R$')
        elif vel > 1.2*vel_max and vel <= 1.5*vel_max:
            print('INFRAÇÃO GRAVE\nMULTA DE 195,23 R$')
        elif vel > 1.5*vel_max:
            print('INFRAÇÃO GRAVÍSSIMA\nMULTA DE 3X195,23 R$\nSUSPENSÃO DO DIREITO DE DIRIGIR E APREENSÃO DO DOCUMENTO')
