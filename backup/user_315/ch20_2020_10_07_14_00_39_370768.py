distancia = float(input('Qual a distância a ser percorrida em km? '))
if distancia <= 200:
    print('O preço ficou {0:.2f}'.format(distancia*0.5))
elif distancia > 200:
    print('O preço ficou {0:.2f}'.format((distancia*0.5) + (distancia-200)*0.45))