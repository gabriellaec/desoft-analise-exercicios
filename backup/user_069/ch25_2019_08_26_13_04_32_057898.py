distancia = float(input('Qual a distância a ser percorrida? '))
if distancia > 200:
    valor1 = 0.5*200 + (distancia - 200)*0.45
    print('O valor será {0:.2f}'.format(valor1))
else:
    valor2 = distancia*0.5
    print ('O valor será {0:.2f}'.format(valor2))