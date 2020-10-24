distancia=int(input('Qual a distância de sua viagem? '))
if distancia<=200:
    preço=distancia*0.50
    print('R${0:.2f}'.format(preço))
else:
    preço=100+(distancia-200)*0.45
    print('R${0:.2f}'.format(preço))
              