dist = int(input('Qual a distância da viagem? '))

if dist<=200:
    preço = dist*0.50
    print('O preço da passagem é de {}'.format(preço))
else:
    distextra = dist-200
    preço = distextra*0.45+100
    print('O preço da passagem é de {}'.format(preço))