distância = int(input('Qual é a distância:'))
if distância <= 200:
    preço = 0.50*distância
    print('{0:.2f}'.format(preço))
else:
    preço = 0.45*distância
    print('{0:.2f}'.format(preço))         