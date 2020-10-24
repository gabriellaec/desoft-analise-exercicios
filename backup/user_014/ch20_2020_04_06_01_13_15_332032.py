distancia = int(input('Qual a distância que você quer percorrer? '))
distancia_maior = distancia - 200

if distancia < 200:
    preco = distancia * 0.50
else:
    preco = 200 * 0.50 + distancia_maior * 0.45

print('O preço da passagem é: R$ {0:.2f}'.format(preco))