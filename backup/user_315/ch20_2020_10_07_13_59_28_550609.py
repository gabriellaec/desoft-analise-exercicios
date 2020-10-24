distancia = float(input('Qual a distância a ser percorrida em km? '))
preco1 = 0.50
preco2 = 0.45

if distancia <= 200:
    print('O preço ficou {0:.2f}'.format(distancia*preco1))
elif distancia > 200:
    print('O preço ficou {0:.2f}'.format((distancia*preco1) + (distancia-200)*preco2))