distância = int(input('Qual é a distância: '))
if distância <= 200:
    preço = 0.50*distância
    print('{0:.2f}'.format(preço))
else:
    preço = (200*0.5) + (0.45*(distância-200)):
    print('{0:.2f}'.format(preço))         