distancia = int(input('Qual a distancia que deseja viajar? '))

if distancia < 200:
    valor = format(distancia*0.5, '.2f')

else:
    valor = format(100 + (distancia-200)*0.45, '.2f')