km = float(input('Qual a distância a ser percorrida em km? '))
if distancia <= 200:
    print('{0:.2f}'.format(km*0.5))
elif distancia > 200:
    print('{0:.2f}'.format((km*0.5)+(km-200)*0.45))